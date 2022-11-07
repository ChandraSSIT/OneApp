# Data types
# Data type
# based on data which is assigned to variable will define type of that particular data
# we have very few data types
# Primitive data types
# string (str) ,int ,float , bool

name = 'python'  # the data which is defined in single quotes or double quotes will be the string type
# by using type we can get the datatype of variable
print("Datatype of name ", type(name))

x = 10  # the data which contains only numerics will be the type of int
print("Datatype of x ", type(x))

balance = 233.23  # the data which contains decimal value will be type of float
print("Datatype of balance ", type(balance))

valid = True  # the data which contains True or False will be type of bool
print("Datatype of valid", type(valid))

# Datatype conversion
# we are converting from one data type to other datatype
# We have two types of data type conversion
# Implicit type conversion
# Explicit type conversion

# Implicit type conversion
# it will automatically convert into higher data type
prinicipl_amount = 10000  # int
interest = 44.33  # float
total = prinicipl_amount + interest  # int+float => float
print(total)
print(type(total))

# Explicit data type conversion
#  we will convert into particular data type
total = prinicipl_amount + int(interest) # int + int => int
print(total)
print(type(total))

address = name + "12/34,ATP,AP" + str(515425)
print(address)
print(type(address))

value = "3344"
output = int(value) + 45  # 3389
print(output)


