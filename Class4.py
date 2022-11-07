# tuple
# it contains sequence of different data type elements, but we can't change the data
# CRUD
# Create => we can achieve
t1 = (2,3,"hdfc","Icici","sbi")
# Read
print(t1)
print(t1[2])
print(t1[3:5])
# 2,hdfc,sbi
print(t1[0:5:2])

# update => tuple will not support
# t1[0] = 34

# delete
# del t1[0] # single element delete will not work
del t1
# print(t1)
# what is difference between list and tuple
# list is mutable(changeable ) , it means we can update elements and delete particular element
# tuple is immutable(un changeable) , it means we can't update elements and we can't delete particular element

# data type conversion
t2 = (2,3,"hdfc","Icici","sbi")
l1 = list(t2)
print(l1)
