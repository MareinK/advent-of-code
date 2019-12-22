import re
addresses = [line.strip() for line in open('7.txt')]
pattern_ssl = re.compile(r'(\w)(?!\1)(\w)\1\w*(?:(\[|\]).*\3|[\[\]])\w*\2\1\2')
ssl = lambda address: pattern_ssl.search(address)
matches = [add for add in addresses if ssl(add)]
print(len(matches))
