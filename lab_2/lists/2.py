#1
list1 = ["apple", "banana", "cherry"]
print(list1[1]) #return banana

#2
list1 = ["apple", "banana", "cherry"]
print(list1[-1]) #return cherry

#3
list1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list1[2:5]) #return ['cherry', 'orange', 'kiwi']

#4
list1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list1[:4]) #return ['apple', 'banana', 'cherry', 'orange']

#5
list1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list1[2:]) #return ['cherry', 'orange', 'kiwi', 'melon', 'mango'] 

#6
list1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list1[-4:-1]) #return ['orange', 'kiwi', 'melon']

#7
list1 = ["apple", "banana", "cherry"]
if "apple" in list1:
  print("Yes, 'apple' is in the fruits list")