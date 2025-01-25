#1
print(10 > 9) #true
print(10 == 9) #false
print(10 < 9) #false

#2
a = 444
b = 74

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#3
#return True
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#return False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#4
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) #False

#5
def myFunction() :
  return True

print(myFunction()) #True

#6
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#7
x = 200
print(isinstance(x, int))