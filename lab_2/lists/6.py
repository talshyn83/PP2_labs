#1
list1 = ["apple", "banana", "cherry"]
for x in list1:
  print(x)

#2
list1 = ["apple", "banana", "cherry"]
for i in range(len(list1)):
  print(list1[i])

#3
list1 = ["apple", "banana", "cherry"]
i = 0
while i < len(list1):
  print(list1[i])
  i = i + 1

#4
list1 = ["apple", "banana", "cherry"]
[print(x) for x in list1]