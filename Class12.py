# Decorators
# To extend the functionality of  a function without modifying , where in python we can pass function as a
# variable

def calculator(fn):
    def inner1(a, b):
        if a > b:
            print("I am from decorator")
            result = fn(a, b)
            print("result from decorator -", result)

    return inner1


@calculator
def sub(a, b):
    return a - b

#
# l = 50
# primenumbers = []
# for i in range(2, 50):
#     for j in range(2, i):
#         if (i % j) == 0:
#             break
#     else:
#         # print(i)
#         primenumbers.append(i)
#
# print('number of prime numbers ', primenumbers)
#
# # positional arguments
# # keyword arguments
# # default arguments
# # arbitrary arguments
# # keyword arbitrary arguments
#
# # def functionaname():
# # break,continue,pass,return,yield
#
# # oops
#
# def sample():
#     for i in range(2,10):
#         yield i
#
#
# for i in sample():
#     print(i)