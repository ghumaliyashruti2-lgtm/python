#abstract method create

print("--->> abstract method create <<---")

class abstract1:
    def abstrcat_fun(self):#method create in parent class
        pass
    
class abstract2(abstract1):
    def abstrcat_fun(self):
        print("i am function of abstract2 class")#but declare in child class
        
class abstract3(abstract1):
    def abstrcat_fun(self):
        print("i am function of abstract3 class")

abstract2obj = abstract2()
abstract3obj = abstract3()

abstract2obj.abstrcat_fun()
abstract3obj.abstrcat_fun()

print("abstract method is created in parent class but its declared in child classes")
