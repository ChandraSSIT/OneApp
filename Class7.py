# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators

# Assignment operators
x = 5
print(x)
# x = x+3
x += 3  # x = x+3
print(x)

x -= 2  # x = x-2
print(x)

x *= 3  # x = x*3
print(x)

x /= 2  # x = x/2

# Comparison operators

x = 5
y = 6

print(x > y)
print(x < y)
print(x == y)
print(x <= y)
print(x >= y)
print(x != y)

# Logical operators
# and ,or , not
print("Logical operator")
# and => both conditions should be true
# or=> any one condtion is true
x = 10
print(x > 4 and x < 9)
x = 8
print(x > 4 and x < 9)
# and
# True and True => True
# False and False => False
# True and False => False
# False and True => False

# or
# True and True => True
# False and False => False
# True and False => True
# False and True => True
x = 10
print(x > 4 or x < 9)
x = 8
print(x > 4 or x < 9)

# not
print("not", not (x > 4 or x < 9))

# Identity operators
x = 5
y = x
print("Identity", x is y)
print("Identity not", not (x is y))

# Membership operators
# in , not in
l1 = [2, 3, 4, 5]
print("Membership operator in ", 2 in l1)
print("Membership operator in ", 6 in l1)
