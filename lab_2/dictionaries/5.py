#1
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict1.pop("model")
print(dict1)

#2
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict1.popitem()
print(dict1)

#3
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del dict1["model"]
print(dict1)

#4
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict1.clear()
print(dict1)