import re
addresses = [line.strip() for line in open('7.txt')]
pattern_abba = re.compile(r'(\w)(\w)(?!\1)\2\1(?![^\[]*\])')
pattern_hyperabba = re.compile(r'(\w)(\w)(?!\1)\2\1\w*\]')
abba = lambda address: pattern_abba.search(address)
hyperabba = lambda address: pattern_hyperabba.search(address)
matches = [add for add in addresses if abba(add) and not hyperabba(add)]
print(len(matches))
