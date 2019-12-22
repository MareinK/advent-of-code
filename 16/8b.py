import difflib, string, re
import numpy as np
import scipy.misc
from PIL import Image, ImageFont, ImageDraw, ImageOps, ImageFilter

instructions = [line.strip() for line in open('8.txt')]
def rect(arr,x,y): arr[:y,:x] = 1
def row(arr,i,n): arr[i] = np.roll(arr[i],n)
def column(arr,i,n): arr[:,i] = np.roll(arr[:,i],n)
actions = {re.compile(r'rect (\d*)x(\d*)'): rect,
           re.compile(r'rotate row y=(\d*) by (\d*)'): row,
           re.compile(r'rotate column x=(\d*) by (\d*)'): column}
arr = np.zeros((6,50));
for instruction in instructions:
  for pattern,action in actions.items():
    match = pattern.match(instruction)
    if match:
      action(arr,*map(int,match.groups()))

#source: http://stackoverflow.com/a/36386628
def char_to_pixels(text, path='arialbd.ttf', fontsize=14):
    font = ImageFont.truetype(path, fontsize) 
    w, h = font.getsize(text)  
    h *= 2
    image = Image.new('L', (w, h), 1)  
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text, font=font) 
    arr = np.asarray(image)
    arr = np.where(arr, 0, 1)
    arr = arr[(arr != 0).any(axis=1)]
    return np.where(arr, 1, 0)

def display(arr):
    result = np.where(arr, '#', ' ')
    print('\n'.join([''.join(row) for row in result]))

size = np.array([5,6])
scale = 1
    
def get_alphabet():
  for c in string.ascii_uppercase:
    arr = char_to_pixels(
        c, 
        path='/usr/share/fonts/TTF/andalemo.ttf', 
        fontsize=26)
    arr = arr[~(np.all(arr==0, axis=1))]
    arr = arr[:,~(np.all(arr==0, axis=0))]
    yield c,scipy.misc.imresize(arr,size[::-1]*scale,interp='bilinear')
    
alphabet = dict(get_alphabet())

def match_letter(char):
  #x = difflib.get_close_matches(char,alphabet.values(),n=1)
  #print(x)
  l = min(alphabet,key=lambda a: np.abs((char-alphabet[a])).sum())
  #display(alphabet[l])
  print(l)
    

#for l,arr in alphabet:
#  print(arr.shape)
#  display(arr)

from tesserocr import PyTessBaseAPI, RIL, iterate_level
import cv2

for i in range(0,arr.shape[1],size[0]):
  char = arr[:,i:i+size[0]]
  display(char)
  char = scipy.misc.imresize(np.pad(char,1,'constant'),10.0,'cubic')
  char = np.float32(char)
  #char = cv2.blur(char
  #char = cv2.medianBlur(char,3)
  image = ImageOps.invert(Image.fromarray(scipy.misc.imresize(char,1.0)))
  #image = image.resize(size*50,Image.LANCZOS)
  #image.show()
  #display(char)
  with PyTessBaseAPI() as api:
    api.SetImage(image)
    api.SetVariable("save_blob_choices", "T")
    api.SetVariable("tessedit_char_whitelist", string.ascii_uppercase+string.ascii_lowercase)
    api.SetVariable("tessedit_pageseg_mode", "10")
    api.Recognize()
    ri = api.GetIterator()
    level = RIL.SYMBOL
    for r in iterate_level(ri, level):
        symbol = r.GetUTF8Text(level)  # r == ri
        conf = r.Confidence(level)
        if symbol:
            print(u'symbol {}, conf: {}'.format(symbol, conf))
        continue
        indent = False
        ci = r.GetChoiceIterator()
        for c in ci:
            if indent:
                print('\t\t ')
            print('\t- ')
            choice = c.GetUTF8Text()  # c == ci
            print(u'{} conf: {}'.format(choice, c.Confidence()))
            indent = True
        print('---------------------------------------------')
    #break
    
# result spells AFBUPZBJPS
