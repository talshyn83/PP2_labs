#1
list1 = ["orange", "mango", "kiwi", "pineapple", "banana"]
list1.sort()
print(list1)

#2
list1 = [100, 50, 65, 82, 23]
list1.sort()
print(list1)

#3
list1 = ["orange", "mango", "kiwi", "pineapple", "banana"]
list1.sort(reverse = True)
print(list1)

#4
list1 = [100, 50, 65, 82, 23]
list1.sort(reverse = True)
print(list1)

#5
def myfunc(n):
  return abs(n - 50)

list1 = [100, 50, 65, 82, 23]
list1.sort(key = myfunc)
print(list1)

#6
list1 = ["banana", "Orange", "Kiwi", "cherry"]
list1.sort()
print(list1)

#7
list1 = ["banana", "Orange", "Kiwi", "cherry"]
list1.sort(key = str.lower)
print(list1)

#8
list1 = ["banana", "Orange", "Kiwi", "cherry"]
list1.reverse()
print(list1)