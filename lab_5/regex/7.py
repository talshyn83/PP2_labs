import re

s = input()
print(''.join(word.capitalize() if i > 0 else word for i, word in enumerate(s.split('_'))))
