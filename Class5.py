# set
# [],(),{}
# it contains different types of data of different data type, but it removes duplicates
set1 = {90, 34, 1, 2, 3, 1, 4, 5, 76, 3, 54}
l1 = [90, 34, 1, 2, 3, 1, 4, 5, 76, 3, 54]
t1 = (90, 34, 1, 2, 3, 1, 4, 5, 76, 3, 54)
print(l1)
print(t1)
print(set1)

# CRUD

# Read
# indexing or slicing will not work
for i in set1:
    print(i)

# update
# we can't update particular element , but we can add new elements
set1.add(190)
set1.update([210, 200])
print(set1)

# delete
# pop
# remove
set2 = {10, 40, 50, 20, 30, 50}
print(set2)
# set2.pop()
set2.remove(50)
print(set2)

l1 = [10, 40, 50, 20, 30, 50]
# l1.pop()
# l1.pop()
l1.remove(50)
print(l1)

del set1

# union,intersection ,intersectionupdate,difference,differenceupdate
set3 = {2, 3, 4, 5, 6}
set4 = {10, 20, 2, 3, 4, 30}
set5 = set4.union(set3)
print("unioin ", set5)

l1 = [2, 3, 4, 5, 6]
l2 = [10, 20, 2, 3, 4, 30]
output = set(l1).union(set(l2))
print(output)

intersection = set4.intersection(set3)
print("intersection ", intersection)
output = set(l1).intersection(set(l2))
print(list(output))

print("set3 ", set3)
print("set4 ", set4)
set3.intersection_update(set4)
print("set4 ", set4)
print("set3 ", set3)

s1 = {10, 20, 40, 50, 60}
s2 = {1, 2, 20, 40, 30}

s3 = s2.difference(s1)
print("difference ", s3)

s1.difference_update(s2)
print("difference update", s1)
