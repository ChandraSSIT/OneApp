name = 'Python'
# inbuilt methods of string
# to make first letter as capital in string
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isupper())
print(name.islower())
print(name.isalpha())

# Primitive datatypes => String,int ,float ,bool
x = 5
balance = 34.44

y, z = 4, 3
print(y, z)
print(z)

# Sequence data types => its combination/collection of different data
# List , tuple ,set ,dictionary
# List => collection of different data of different data types
# CRUD => Create Read Update Delete

# Create list
# Create
name = "Veeresh"
x = 10
customer_detail = [name, x, balance, "Chandra"]

print(type(customer_detail))
# pep8 standards => coding standards

# Read
print(customer_detail)
# Individual data
# indexing
print(customer_detail[0])
print(customer_detail[2])
print(customer_detail[3])
print(customer_detail[1])

print(len(customer_detail))

l1 = [10, 20, 22, 34, 4, 5, 44, 56, 6, 6, 445, 67, 35, 64, 6, 4, 633, 22]
total_count = len(customer_detail)
print(total_count - 1)

# Negative indexing
print(customer_detail[-1])
print(l1[-2])
print(l1[-8])
print(l1[- len(l1)])

# slicing
#
# Start index,end-index,step size
#
# Start index = from which position I need to take it
# End index = where I need to stop , but it will consider -1 of the end index
# Step size = by default it will be 1, if I will give 2
print(l1[0:4])  # internally it will consider as l1[0:3-1] means l1[0:2] , here step size will take default value
# as 1 , it considers as l1[0:4:1]
print(l1[0:4:1])
print(l1[0:4:2])
print(l1[0:4:3])
print(l1[0:4:4])

print(l1[5:])
print(l1[5::2])
l1 = [10, 20,6, 4, 633, 22]
print(l1[2:1])
print(l1[2:3])
print(l1[-3:])
print(l1[15:])
print(l1[-3:-1]) #-1-1 [-3:-2]
print(l1[-3:-4])
print("2 to 1 " ,l1[2:0:-1])

# update
# append => to add single element we will use
# extend => to add multiple elements
l1.append("Veeresh")
l1.append(["chandra","mohan"])
print(l1)
l1.extend("Veeresh")
l1.extend(["harish","John"])
print(l1)
l1[6] = "Shaik"
print(l1)
l1[5:7] = 34,"Basha","Purandhar"
print(l1)
l1[8][0]= "RCM"
print(l1)
l1[8] = "ChandraMohan"
print(l1)
print(len(l1))
print(l1.index("ChandraMohan"))
# Delete

del l1[0]
print(l1)
del l1[1:3]
print(l1)
# to delete complete list
del l1
print(l1)







