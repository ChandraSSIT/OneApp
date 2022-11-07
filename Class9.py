# loop statements
# for,while
l1 = ["chandra", "shaik", "Veeresh", "Sai", "Rajitha", "Pavan", "Purushotham", "Purandhar", "Nithin"]

s1 = {2, 3, 4, 1, 2, 3}
for name in l1:
    print(name)

for i in s1:
    print(i)

# range => startindex,endindex,stepsize
for i in range(0, 4):
    print(i, end=" ")

print("")

print("chandra", "veeresh", "harish")
for i in range(0, len(l1), 2):
    print(i, "-", l1[i], end=" ---- ")

print("")
# while
# combination of if and for
x = 10

while x > 8:
    print(x)
    x -= 1  # x = x-1

# 1 to 20 by using while
# by using for
x = 1
while x <= 20:
    print(x, end=" ")
    x += 1

print("")

for i in range(1, 21):
    print(i, end=" ")
else:
    pass

# pass => when we are defined any code then we can use pass keyword to continue

# pass , break , continue ,return

print("break  example")
# break
# if we want to break/stop the iteration in the middle of execution , it will stop the execution and comes
# out of loop


l1 = ["chandra", "shaik", "Veeresh", "Sai", "Rajitha", "Pavan", "Purushotham", "Purandhar", "Nithin"]

for i in l1:
    if i == "Sai":
        print(i)
        break
    else:
        print(i, end=" ")

print("")
for i in range(1, 4):
    if i == 3:
        break
    print(i, end=" ")

else:
    print("else block executed")

# when the  iteration completes without any break/interruption , then else block will execute
print("")
# continue  =>  it will skip the current iteration and move on next iteration
l1 = [2, 8, 1, 27]
for i in range(1, 30):
    if i in l1:
        continue

    print(i, end=" ")

customers = [{"name": "harish", "salary": 23344, "id": 232}, {"name": "Veeresh", "salary": 23344, "id": 232},
             {"name": "Pavan", "salary": 23344, "id": 232}, {"name": "Purandhar", "salary": 23344, "id": 232}]

print("")
for i in customers:
    if i["name"] == "Pavan":
        print(i)
        break


