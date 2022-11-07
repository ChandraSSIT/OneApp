# Polymorphism
# defining same function with different signature
# Overloading
# Overriding

# Is python supports overloading  => No

def add(*args):
    total = 0
    for i in args:
        total += i
    print(total)


# def add(a,b,c):
#     return a+b+c


add(2, 3)
add(3, 4, 5)
# MRO => Method resolution order

# we can achieve overloading by using *args ,**kwargs

from multipledispatch import dispatch

class calculator:

    @dispatch(int,int)
    def add(self, a, b):
        print( "Overloading with two parameters " ,a + b)

    @dispatch(int,int,int)
    def add(self, a, b, c):
        print("Overloading with three parameters ",a + b + c)


obj = calculator()
obj.add(2,3)
obj.add(3,4,5)

# Using *args,**kwargs,by using multipledispatch module

# Inheritance
# Its parent and child relation

class Parent:
    def get_lands(self):
        print("2 lands from father")


class Child(Parent):

  def get_buildings(self):
      print("1 building")

  def get_lands(self):
      print("you sold all lands")


obj = Child()

obj.get_lands()
obj.get_buildings()

# Overriding => it will support overriding => defining same function in child class by using inheritance
# Overloading => it will not support

