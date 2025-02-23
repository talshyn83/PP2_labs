import re

s = input()
print(bool(re.fullmatch(r'[A-Z][a-z]+', s)))
