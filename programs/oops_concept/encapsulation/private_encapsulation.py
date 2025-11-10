# private variable achive in encapsulation

print(" ---->>> private variable achive in encapsulation <<<------\n")

print(" -> class 1 :- private_encapsul1")
class private_encapsul1:
    def __init__(self,a):
        self.__a = a #here use __ for make a privte variable 
    def display1(self):
        print("private variable in a display1 method in class of private_encapsul1 :",self.__a)

print(" -> class 2 :- private_encapsul2 ")
class private_encapsul2(private_encapsul1):
    def __init_(self,b):
        super().__init__(b)
    def  display2(self):
        print("private variable in a display1 method in class of private_encapsul1 :",self.__a)

priencobj = private_encapsul2(10)
priencobj.display2()

print("private property of parent class or other class is not achive in any class ")
