#1
list1 = ["apple", "banana", "cherry"]
list1.append("orange")
print(list1)

#2
list1 = ["apple", "banana", "cherry"]
list1.insert(1, "orange")
print(list1)

#3
list1 = ["apple", "banana", "cherry"]
list2 = ["mango", "pineapple", "papaya"]
list1.extend(list2)
print(list1)

#4
list1 = ["apple", "banana", "cherry"]
list2 = ("kiwi", "orange")
list1.extend(list2)
print(list1)