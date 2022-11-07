# Single level inheritance
# Multilevel inheritance
# Multiple inheritance

# Single level inheritance
class father:
    def get_properties(self):
        print("father building properties")


class mother:
    def get_properties(self):
        print("mother building properties")

    def get_motherproperties(self):
        print("mother properties")

class wife:
    def get_wife_properties(self):
        print("wife properties")

# Multiple Inheritance

from multipledispatch import dispatch

class child(father,mother,wife):
    def get_my_own_properties(self):
        print("1 land")

    def get_motherproperties(self):
        print("sold mother properties")

    # def get_properties(self):
    #     print("sold all buildings")


obj = child()
obj.get_properties()
obj.get_wife_properties()
obj.get_motherproperties()
obj.get_my_own_properties()
