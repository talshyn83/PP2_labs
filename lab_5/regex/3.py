import re

s = input()
print(bool(re.fullmatch(r'[a-z]+_[a-z]+', s)))
