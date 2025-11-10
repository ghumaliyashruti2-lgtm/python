#method overloading

print("--->> method overloading :- same name and argument but different class <<---")


class methodoverriding1:
    #function with no argument 
    def mriding_fun(self,a):
        print("i am method of class methodoverriding1")
        
class methodoverriding2(methodoverriding1):
    def mriding_fun(self,a):
        super().mriding_fun(10)
        print("i am method of class methodoverriding2")

class methodoverriding3(methodoverriding2):
    def mriding_fun(self,a):
        super().mriding_fun(10)
        print("i am method of class methodoverriding3 ")
        
mridingobj = methodoverriding3()
mridingobj.mriding_fun(10)


        
