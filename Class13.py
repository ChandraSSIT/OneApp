from Class12 import sub
import math

print(math.factorial(6))

sub(6, 5)

# global ,local

x = 10
a = 40


def samplelocalglobal():
    # y=20
    # global z
    # z=30

    global a
    a = 30
    print("from function a ", a)
    # print("from function ",x)
    # print("from function y ",y)


print("from outside a", a)
samplelocalglobal()
print("from outside a", a)
# print("from outside ",x)
# print("from outside access local variabe ",z)

# OOPS

# object-oriented programming structure
# class,object,abstraction,encapsulation,polymorphism,inheritance

# Class => class is nothing but container , which contains members and member functions
class bank:
    bank_name = "ICICI"
    ifsccode = "ICIC002"
    address = "ATP"



# object => Instance of a class

bankObj = bank()
print(bankObj.bank_name)
print(bankObj.ifsccode)
bankObj.ifsccode ="ICIC3323"
print(bank.address)
print(bankObj.ifsccode)









