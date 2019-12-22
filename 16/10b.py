import collections,re

value_pattern = re.compile(r'value (\d*) goes to (\w* \d*)')
action_pattern = re.compile('(\w* \d*) gives low to (\w* \d*) and high to (\w* \d*)')
actions = collections.OrderedDict()
chips = collections.defaultdict(list)

instructions = [l.strip() for l in open('10.txt')]
for instruction in instructions:
  value_match = value_pattern.match(instruction)
  if value_match:
    chip,out = value_match.groups()
    chips[out].append(int(chip))
  action_match = action_pattern.match(instruction)
  if action_match:
    bot,low,high = action_match.groups()
    actions[bot] = (low,high)

    
comparisons = collections.defaultdict(list)
comp_len = None
def changed():
  global comp_len
  new_comp_len = sum(map(len,comparisons.values()))
  r = comp_len != new_comp_len
  comp_len = new_comp_len
  return r

while changed():
  for frm,to in actions.items():
    if len(chips[frm]) == len(to):
      chips[frm] = sorted(chips[frm])
      comparisons[tuple(chips[frm])].append(frm)
      for chip,out in zip(chips[frm],to):
        chips[out].append(chip)
      chips[frm] = []
      
print(chips['output 0'][0]*chips['output 1'][0]*chips['output 2'][0])
