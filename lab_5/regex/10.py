import re

with open(r"C:\Users\binur\OneDrive\Рабочий стол\PP2_labs\lab_5\row\row.txt", encoding="utf-8") as f:
    data = f.read()

modified_data = re.sub(r'(?<!^)(?=[A-Z])', '_', data).lower()
print("10:", modified_data)