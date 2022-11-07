# class methods,instance methods,static methods
class A:
    # Class variable
    firstname= "abc"
    def __init__(self):
        self.lastname ="xyz"

    def M7(self):
        print("M7 ")

    def M1(self):
        # Local variable
        address="ATP"
        self.surname ='MMM'
        self.M7()
        self.M2()
        print("M1")

    @staticmethod
    def M3(self):
        print("M3 static method")

    @staticmethod
    def M2():
        print("from static method M2")

    @classmethod
    def M4(cls):
        print(cls.firstname)
        cls.M1(cls)
        cls.M2()
        print("Class Methods")


# Instance variables => The variables which are accessed by using object is called , we will create by using
# self
# Instance method => The method which are accessed by using object is called instance method
obj = A()
# obj.M1()
# print(A.firstname)
# obj.lastname
# obj.surname
#
# # Static methods => which are accessed without object directly with class
# A.M2()
# A.M3("Test")

# Class Methods =>
# we can access class methods with or without object
# we can access class variables
# we can access instance method but by passing object instance
# we can access static methods
# we can not access instance variables

obj.M1()
# A.M4()

# Datetime functions,Regular expressions, file handling, error handling


