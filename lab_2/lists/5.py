#1
list1 = ["apple", "banana", "cherry"]
list1.remove("banana")
print(list1)

#2
list1 = ["apple", "banana", "cherry", "banana", "kiwi"]
list1.remove("banana")
print(list1)

#3
list1 = ["apple", "banana", "cherry"]
list1.pop(1)
print(list1)

#4
list1 = ["apple", "banana", "cherry"]
list1.pop()
print(list1)

#5
list1 = ["apple", "banana", "cherry"]
del list1[0]
print(list1)

#6
list1 = ["apple", "banana", "cherry"]
del list1

#7
list1 = ["apple", "banana", "cherry"]
list1.clear()
print(list1)