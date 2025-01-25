#1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
list1 = []

for x in fruits:
  if "a" in x:
    list1.append(x)

print(list1)

#2
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

list1 = [x for x in fruits if "a" in x]

print(list1)

#3
list1 = [x for x in fruits if x != "apple"]

#4
list1 = [x for x in fruits]

#5
list1 = [x for x in range(10)]

#6
list1 = [x for x in range(10) if x < 5]

#7
list1 = [x.upper() for x in fruits]

#8
list1 = ['hello' for x in fruits]

#9
list1 = [x if x != "banana" else "orange" for x in fruits]