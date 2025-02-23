import re

s = input()
print(bool(re.fullmatch(r'a.*b', s)))
