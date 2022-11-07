class bank:
    bank_name = "ICICI"
    ifsccode = "ICIC002"
    address = "ATP"

    def get_bank_details(self):
        self.branch_code = "BRC12323"
        return self.bank_name + " " + self.ifsccode + " " + self.branch_code

    def get_bank_location(self, location="MUM"):
        return self.get_bank_details() + " " + location

    # self => It represents current instance of a class


bankObj = bank()
bankObj.bank_name

print(bankObj.get_bank_details())
print(bankObj.branch_code)
print(bankObj.get_bank_location("BLR"))

# oops =>object-oriented programming structure
# class ,object ,abstraction,encapsulation,polymorphism,inheritance
# class => class is a container which contains members and member functions
# self => represents current instance of class => it will use current object
class sample:
    firstname ="chandra"
    accountno = 1232323

    def add(self):
        print(self.firstname +" " +str(self.accountno))
        print("add function")

# object => instance of a class => we are creating instance of class and while creating it will allocate
# memory
obj = sample()
print(obj.firstname)
obj.firstname ="mohan"
print(obj.add())

