# private variable achive in encapsulation

print(" ---->>> protected variable achive in encapsulation <<<------\n")

print(" -> class 1 :- procted_encapsul1 ")
class procted_encapsul1:
    def __init__(self,a):
        self._a = a #here use __ for make a protected variable 
    def display1(self):
        print("protected variable in a display1 method in class of procted_encapsul1 :",self._a)

print(" -> class 2 :- procted_encapsul2 ")
class procted_encapsul2(procted_encapsul1):
    def __init_(self,b):
        super().__init__(b)
    def  display2(self):
        print("protected variable in a display1 method in class of procted_encapsul2 :",self._a)

proencobj = procted_encapsul2(10)
proencobj.display2()

print("protected property of parent class or other class is achive by child ")
