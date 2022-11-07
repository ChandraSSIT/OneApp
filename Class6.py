# List => []
# Tuple => ()
# Set => {}
# dictionary => {}

customer = ['Chandra', 123223, 223, "ATP"]

# CRUD
# Create
# dictionary is a key and value pair
customer = {"Name": 'chandra', "account": 1233444, "balance": 23344, "address": "ATP"}

# key should be unique ,and key should not be duplicate . In case if we have a duplicate key ,
# the latest value  will override
# Read
print(customer['Name'])
print(customer['address'])
print(customer.keys())
print(customer.values())
print("")
print("dictionary items - ", customer.items())
print("")
# update
customer['address'] = "BLR"
print(customer)
customer['pincode'] = 515001
print(customer)

# delete
del customer['Name']
print(customer)
# del customer
customer.pop('pincode')
print(customer)
customer.clear()
print(customer)

# list,tuple,set,dictionary
# list  => it's a mutable , elements will be changeable
# tuple => immutable , we can not change
# set => it removes duplicate
# dictionary => key and value pair
# string,int,float,bool
# string => immutable

# operators
# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators

# Arithmetic operators
# +,-,*,/,% ,//

a = 2 + 3  # 5 # addition
b = 3 - 2  # 1 # subtraction
c = 3 * 2  # 6  # multiplication
d = 4 / 2  # 2 # division
e = 3 % 2  # 1 => remainder #modulation
f = 2 ** 3 # 2*2*2 => 2 power of 3 # exponentiation
g = 154 // 10 # floor division => 15 , it will remove decimal after division
print(g)

