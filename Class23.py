# Regualar expression

import re
str1 ="hi hello word hi how are hi 1 3  4 "

data  = str1.split(" ")
print(data)
l1 =[]
for i in data:
    if i == "hi":
        l1.append(i)
print(len(l1))

pattern = re.compile(r'\bhi\b')

print(re.findall(pattern,str1))

#  IP Address match
str2 ="My ip address is 10.20.20.234 this is static ip address 10.39.40 "

pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]')

print("IP Address match ", re.findall(pattern,str2))

# Email

str3  =" hi my email is chandra.mohan@gmail.com hello "

pattern3 = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

print( "email ids - " ,re.findall(pattern3,str3))
# re.findall() => this will give complete matching list
# re.search() => this will give first occurrence of matched string
# re.match() => this will give true or false

# def valid(ip):
#     data = ip.split()
#     for i in data:
#         for j in i:
#             if str(j).isdigit() :
#                 return False
#             else:
#                 if int(j) >0 and int(j) <=255:
#                     pass
#
# valid('30.33.333.23')
# valid('23.sdd.fd.233')
# valid('233.33.')

# Python
# Variables,Datatypes(string,float,int,bool)
# Datatype conversion
# sequence datatypes(List,tuple,dictionary,set)
# operators
# conditional statements (IF ELIF ELSE)
# flow controls (for loop, while loop)
# break,continue , return , pass
# functions
# types of arguments
# iterators
# generators
# decorators
# function inside function
# oops
# class
# object
# abstraction
# encapsulation
# polymorphism
# inheritance
# date time module
# file handling
# exception handling (try except finally)
# Regular expression

# check prime number
# factorial of number
# fibonacci series of number
# find element from list
# even number
# reverse string



