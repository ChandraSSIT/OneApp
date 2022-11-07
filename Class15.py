# constructor ,abstraction ,encapsulation

class bank:

    # magic methods
    # default ,parameterized
    # default constructor
    def __init__(self,bank_Name,ifsc,bank_Address,password):
        self.bank_name = bank_Name
        self.ifsccode = ifsc
        self.__address = bank_Address
        self.__password = password

    def get_bank_details(self):
        self.branch_code = "BRC12323"
        return self.bank_name + " " + self.ifsccode + " " + self.__address+" "+ self.branch_code

    def get_bank_location(self, location="MUM"):
        return self.get_bank_details() + " " + location

    # # destructor
    # def __del__(self):
    #     print("desctructor")


bankObj = bank("HDFC","HDFC12332","BLR")
print(bankObj.get_bank_details())

print("//////")
iciciobj = bank("ICICI","ICIC1222","BLR")
print(iciciobj.bank_name)
# print(iciciobj.address)
print(iciciobj.ifsccode)

# del iciciobj
# # print(iciciobj)

# abstraction => exposing the details to outside by hiding the logic
print(iciciobj.get_bank_location())
# encapsulation => hiding the details , hiding members or member function from outside
# by making them as private
# in python we will use __
