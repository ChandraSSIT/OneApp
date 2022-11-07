def add(a, b):
    return a + b


customers = [{"name": "Pavan", "Account": 1232133, "bank": "HDFC", "cusid": 765566},
             {"name": "Veeresh", "Account": 9865335, "bank": "HDFC", "cusid": 87666},
             {"name": "sai", "Account": 35762555, "bank": "HDFC", "cusid": 56655}]


def get_customer(cusid):
    for i in customers:
        if i["cusid"] == cusid:
            return i

    return "No details found"

# Positive scenarios
# negative scenarios
# boundary scenarios

# we have to use pytest framework to automate test cases
# install pytest => pip install pytest
# the file names should start with test_
# the test methods names inside file should start with test

# commands to use to execute test cases , from terminal we need to execute
# pytest -v
# -v will give the in details about each test
# we can group the test cases by using mark functionality
# @pytest.mark.groupname
# will execute by using pytest -m -v

# If I want to execute based on test method name
# pytest -k -v

# we have mark called parametrized , by using this we can execute same method with different input and output
