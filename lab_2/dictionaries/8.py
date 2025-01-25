#1
myfamily = {
  "child1" : {
    "name" : "Binur",
    "year" : 2007
  },
  "child2" : {
    "name" : "Nurai",
    "year" : 2008
  },
  "child3" : {
    "name" : "Beka",
    "year" : 2011
  }
}

#2
child1 = {
  "name" : "Binur",
  "year" : 2007
}
child2 = {
  "name" : "Nurai",
  "year" : 2008
}
child3 = {
  "name" : "Beka",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#3
print(myfamily["child2"]["name"])

#4
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])