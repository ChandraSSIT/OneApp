# functions
# it's a block of code which we will be reused
a = 2 + 3
b = 4 + 5
a = 6 + 7
a = 8 + 7


# defining a function
# for that we need use def as key word , function name , parameters/arguments
# syntax => def functionnamme() :
def sample():
    print("Test sample")
    print("I am writing first function")
    print("default parameter")


# how to use/call this function
# function without parameters
sample()
sample()


# parameters => what data you want to pass will be defined here , how many types of data
def add(a, b):
    print(a + b)


add(2, 3)
add(3, 4)
add(7, 6)

customers = []


def bankcustomers(name, accountno, amount, ifsccode):
    customer = {"Name": name, "AccountNo": accountno, "Amount": amount, "IFSCCode": ifsccode}
    customers.append(customer)


bankcustomers("john", 122332, 20000, "ICICI1223")
bankcustomers("Kelly", 122332, 30000, "SBI1223")
bankcustomers(122332, "chandra", 30000, "SBI1223")

bankcustomers(amount=12000, ifsccode='HDFC133', name='mohan', accountno=2343)

print(customers)

# positional arguments/parameters
# named/keyword arguments
# default arguments
# arbitrary arguments
# keyword arbitrary arguments

# def subtract()
# def createaadhardetails()
# def getmyaadhardetails(aadharnumber)

all_user_details = []


def create_aadhar_details(aadhar_number, name, address):
    aadhar_details = {"aadharnumber": aadhar_number, "name": name, "address": address}
    all_user_details.append(aadhar_details)


def get_my_aadhar_details(aadhar_number):
    for i in all_user_details:
        if i["aadharnumber"] == aadhar_number:
            print(i)
            break


# default arguments/parameters
def calculate_bank_interest(principle_amount, years, interest_rate=0.05):
    calculate = principle_amount + (principle_amount * years * interest_rate)
    return calculate


calculate_bank_interest(10000, 1)
calculate_bank_interest(20000, 1)
calculate_bank_interest(30000, 1, 0.04)


# arbitrary arguments

def add(*args):
    total = 0
    for i in args:
        total += i
    print(total)


add(2, 3)
add(3, 4, 5)
add(4, 5, 6, 6, 7, 7)


# keyword arbitrary arguments

def customerdetails(**kwargs):
    for i in kwargs.items():
        print(i)


customerdetails(name="Chandra", Id=123)
print("---")
customerdetails(name="Harish")
print("---")
customerdetails(name="Veeresh", amount=1233)


def all_arguments(name, id1,pincode=515425, *args, **kwargs,):
    print(name, id1, pincode, args, kwargs)

all_arguments("chandra",1333,)

# return
print("return example")

def calculate_bank_interest(principle_amount, years, interest_rate=0.055):
    calculate = principle_amount + (principle_amount * years * interest_rate)
    return calculate
    print("After return")


amount = calculate_bank_interest(10000, 1)
print("total amount for customer",amount)

