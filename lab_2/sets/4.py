#1
set1 = {"apple", "banana", "cherry"}
set1.remove("banana")
print(set1)

#2
set1 = {"apple", "banana", "cherry"}
set1.discard("banana")
print(set1)

#3
set1 = {"apple", "banana", "cherry"}
x = set1.pop()
print(x)
print(set1)

#4
set1 = {"apple", "banana", "cherry"}
set1.clear()
print(set1)

#5
set1 = {"apple", "banana", "cherry"}
del set1
print(set1)