#1
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#2
tuple1 = ("apple", "banana", "cherry")
y = list(tuple1)
y.append("orange")
tuple1 = tuple(y)

#3
tuple1 = ("apple", "banana", "cherry")
y = ("orange",)
tuple1 += y

print(tuple1)

#4
tuple1 = ("apple", "banana", "cherry")
y = list(tuple1)
y.remove("apple")
tuple1 = tuple(y)