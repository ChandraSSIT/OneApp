from multipledispatch import dispatch


@dispatch(int, int)
def add(a, b):
    return a + b


@dispatch(int, int, int)
def add(a, b, c):
    return a + b + c


print(add(1, 2))
print(add(2, 3))


# Single level , MUltiple ,Multilevel

# Multilevel

class A:
    def M1(self):
        print("M1 from class A")


class B(A):
    def M2(self):
        print("M2 from class B")

    def M1(self):
        print("M1 from class B")


class C(B):
    def M3(self):
        print("M3 from class C")

    # def M1(self):
    #     print("M1 from class C")


obj = C()
obj.M1()
obj.M2()
obj.M3()

print('///// super ////')


class X:
    def __init__(self):
        print(self)

    def Func1(self):
        print("from X funct1")


class Z:
    def __init__(self):
        print(self)

    def Func1(self):
        print("from Z funct1")


class Y(X, Z):

    def __init__(self):
        print(self)

    def Funct2(self):
        print("from Y funct2")

    def Func1(self):
        print("from Y funct1")
        super().Func1()
        X.__init__(self)
        Z.__init__(self)
        X.Func1(self)
        Z.Func1(self)


obj = Y()
obj.Func1()
# print(obj)


# class,object,abstraction,encapsulation,constructor,self,super,polymorphism(Overloading,Overriding),
# Inheritance(Single level,Multiple,Multilevel)
# Re usability ,memory management, scalability

