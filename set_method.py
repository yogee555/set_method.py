# SET Method
# add()
dwaves = {"thorin","balin","dwalin"}
dwaves.add("gimli")
print(dwaves)                                   # add one data

# clear()
dwaves1 = {"thorin","balin","dwalin"}
dwaves1.clear()
print(dwaves1)                                 # clear all data

# pop()
dwaves2 = {"thorin","balin","dwalin"}
dwaves2.pop()
print(dwaves2)                                  # remove last data

# union()
dwaves3 = {"thorin","balin","dwalin"}
dwaves4 = {"thorin","balin","dwalin","gimli"}
dwaves5 = {"fili","kili"}
print(dwaves3.union(dwaves4,dwaves5))       # union of data

# copy()
seta = {11,12,20,30}
setb = seta.copy()
print(setb)                                     # copy one data to another data

# set discard
dwaves1 = {"thorin","balin","dwalin"}
dwaves1.discard("balin")
print(dwaves1)                                   # dicard one data

# difference()
dwaves6 =  {"thorin","balin","dwalin"}
dwaves7 = {"gimil","balin","thorin"}
dwaves8 = dwaves6.difference(dwaves7)
print(dwaves8)                                   # difference of stirage data

# intersection()
num1 = {10,15,25,30,45,55}
num2 = {10,20,30,40}
print(num1.intersection(num2))                   # intersection of two storage variable

# isdisjoint
num1 = {17,22,80}
num2 = {12,17,56,80,92}
print(num1.isdisjoint(num2))                     

# issubset
a = {20,40,50}
b = {10,30,60}
f = a.issubset(b)
print(f)
h = b.issubset(a)
print(h)