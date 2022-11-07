# Variables , Data types ,flow controls ,functions , OOPS
# Variables => it stores data in memory

# comments  => providing explanation about the line of code
x = 10  # int
name = 'vamsi'  # which ever is there in double quotes => string
balance = 100.44  # which ever is there in decimal values => float
ispersonexists = False  # bool

print(x)
print(name)

# data types
# types => string ,int ,float , bool
print(type(x))
print(type(name))
print(type(balance))
print(type(ispersonexists))

# primitive data types => string ,int ,float,bool
# sequence data type => this is nothing but grouping of different data types
# list, tuple, set ,dictionary
# we can perform some operations like CRUD => create , read , update ,delete

# Create
l1 = [10, "vamsi", 1000.33, "ATp", "55555"]
l2 = [x, name, balance]

# read
# indexing
# slicing

# indexing is nothing but counting , it will start from 0
# in list l1 => it will start from 0 to length - 1

print(l1[0])
print(l1[1])
print(l1[2])
print(l1[-1])
print(l1[-3])
# positive , negative

# slicing  => starting point and ending point => start index => index
# start index => start position
# end index => value -1 => if we give 2 it will take 2-1 =>1
print("slicing ", l1[0:2])  # l1[0:1]
# step size

print("step size", l1[0:3:2])

# update
print(l1)
l1[0] = 40
l1[0:2] = 30, "chandra"
print(l1)

# delete
del l1[0]
print(l1)
del l1[0:2]
print(l1)
# del l1
# print(l1)

# append ,extend
# append => we can add single element
# extend => we can add list
l1.append("BLR")
print(l1)
l1.extend([2333, "accenture"])
print(l1)

# tuple => its a constant
# create , read
# update => will not work
# delete => we can not delete single element , we can delete complete tuple

# Create
t1 = (x, name, balance, "ATP", "1223")
# read
# indexing ,slicing
print(t1)
print(t1[0])
print(t1[0:3])
# update => it will not work
# t1[0] = 30

# delete
# del t1[0] it will  not support
# del t1
# print(t1)

# list vs tuple
# list => changeable => mutable
# tuple => immutable => unchangeable => update and item deletion will not work , we can not add new items

# set =>
# create
set1 = {91, 20, 1, 2, 3, 1, 2}
# it will automatically remove duplicate data
print(set1)
# read => we can not read with indexing or slicing
for i in set1:
    print(i)
# update => will not work
# delete => will not work with index
set1.remove(91)
print(set1)

# dictionary
# key and value pair
# create
dict1 = {"id": 2323, "name": "chandra", "balance": 20000, "pincode": 515001}


# read
print(dict1.keys())
print(dict1.values())
print(dict1.items())
# update
dict1["id"] = 100
print(dict1)
dict1["address"] = "ATP"
print(dict1)

# delete
del dict1["id"]
print(dict1)

# list [] ,tuple () , set {} ,dictionary{"key","value"}

# conditional statements
# if ,elif else
# flow controls
# for
# while

a = 30
b = 20

if a==b :
   print("a and b are equal")
elif a>b:
    print("a is greater than b")
elif a<b:
    print("a is lesser than b")
else:
    print("both are not equal")

#  for
l1 = [1,2,4,5,6]

for i in l1:
    print(i)

# while
# condtion check

x = 10
while x > 5: #condition true => then it will execute , it will not
    print(x)
    x = x-1

# functions
# its a block of code which can be reuse

# declaration of function
def add(a,b):
    print(a+b)

# calling of function
add(3,4)
add(5,6)
add(5,7)




