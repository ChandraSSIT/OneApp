# Conditional statements
# Loop statements

# Conditional statements =>
# if
x = 5
if x > 4:  # if True
    print("My number is greater than 4")

elif x > 3:
    print("My number is greater than 3")

if x > 2:
    print("My number is greater than 2")
elif x > 1:
    print("My number is greater than 1")

# indent => 4 spaces

x = 9
if x > 10:
    print("greater than 10")
elif x > 11:
    print("greater than 9")
else:
    print("number is less than 10")


isaccountexists = True
accountbalance = 122
withdraw =1000
if isaccountexists:
    if accountbalance >= withdraw:
        print("transfer money")
    else:
        print("Sufficient balance is not available")


