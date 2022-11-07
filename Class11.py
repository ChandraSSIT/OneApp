# function inside function

def sample():
    def inner1():
        print("Inside inner function")

    return inner1


fn = sample()
print(fn())

# iterator,generator, decorator
# iterator => it will iterate through the items by using iter and next functions
# this is the concept behind for loop
# it will complete data in the memory
l1 = [1, 2, 3]

iterobj = iter(l1)
print(next(iterobj))
print(next(iterobj))
print(next(iterobj))
# print(next(iterobj))

# Generators => it will not keep every thing in memory by using yield keyword it will return and continue
def sample():
   yield 1
   yield 2
   yield 3
   print("Completed my generator")



for i in sample():
    print(i)

def sample():
    l1= []
    for i in range(1,100):
      yield i


for i in sample():
    print(i)

# Decorator

# write function to find number is even or not
# write a function to check number is primenumber or not
# write a function to give list of prime numbers from 1 to 50
#
dict1= {
  "time": {
    "updated": "Oct 11, 2022 10:35:00 UTC",
    "updatedISO": "2022-10-11T10:35:00+00:00",
    "updateduk": "Oct 11, 2022 at 11:35 BST"
  },
  "disclaimer": "This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
  "chartName": "Bitcoin",
  "bpi": {
    "USD": {
      "code": "USD",
      "symbol": "&#36;",
      "rate": "19,068.6331",
      "description": "United States Dollar",
      "rate_float": 19068.6331
    },
    "GBP": {
      "code": "GBP",
      "symbol": "&pound;",
      "rate": "15,933.5972",
      "description": "British Pound Sterling",
      "rate_float": 15933.5972
    },
    "EUR": {
      "code": "EUR",
      "symbol": "&euro;",
      "rate": "18,575.6326",
      "description": "Euro",
      "rate_float": 18575.6326
    }
  }
}

# from this dictionary need total of rate_float.

def check_is_even(num):
    # num = int(input(" function to find number is even or not:"))
    if (num % 2) == 0:
        return True
    else:
        return False

print(check_is_even(3))

total = 0
for i in dict1["bpi"]:
    total += dict1["bpi"][i]['rate_float']

print(total)


