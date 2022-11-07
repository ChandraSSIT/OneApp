# File handling
# create a new file and put some data into it
file1 = open("sample.txt","w")
file1.write("Hi Folks how are you doing")
file1.close()

# context management => once your done with job , object will dispose automatically . in python we have called
# with we can achieve this
with open("sample.txt","r") as file2:
    print(file2.read())

with open("sample.txt","a") as file3:
    file3.write(" New data appended")

with open("sample.txt","r") as file4:
    print(file4.read())

# W => write
# R => Read
# a => append

with open("test.txt","r+") as file5:
    print(file5.read())
    file5.write("Hi Python ")
    # file5.seek(0)
    # print(file5.read())

with open(r"C:\Personal\newfile.txt","a+") as file5:
    print("reading initally : ",file5.read())
    file5.write("Hey Friends welcome to organization ")
    file5.seek(0)
    print(file5.read())

