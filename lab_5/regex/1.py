import re

with open(r"C:\Users\binur\OneDrive\Рабочий стол\PP2_labs\lab_5\row\row.txt", encoding="utf-8") as f:
    data = f.read()

matches = re.findall(r'ab*', data)
print("1:", matches)
