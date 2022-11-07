# Excecption handling

# Exception => which can be handled by code
# Error => which can not be handled by code
# try , except, finally
def sample(str1):
    if str1 == None:
        raise Exception("The attribute has None type")
    print(str1.upper)

file1 = open("sample.txt","r")
try:
    y = 0
    x = 5 / 1

    # str1 = None
    # print(str1.upper())
    sample(None)
    file1.read()
    file1.close()
except ZeroDivisionError as ex :
    print("error occured :",ex)

except Exception as ex:
    print(ex)

finally:
    file1.close()
    print("finally block")


customers = [{"name":'chandra',"id":123,"accountno":12333},{"name":'Veeresh',"id":355},
             {"name":'Sai',"id":56,"accountno":98876},
             {"id":45,"accountno":87566}]

def bankcustomer():
        for i in customers:
            try:
               print(i["name"] + " --- " + str(i["accountno"]))
            except Exception as ex:
                print("Error occured :",ex)

bankcustomer()
