import bs4
import requests

page = requests.get('https://aoc.infi.nl/')
soup = bs4.BeautifulSoup(page.text, 'html.parser')

print(soup)

for el in soup.findAll('a', href=True):
    print(el)
