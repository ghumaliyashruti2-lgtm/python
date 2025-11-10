#method overloading

print("--->> method overloading <<---")


class methodoverloading:
    #function with no argument 
    def mloading_fun(self):
        print("no argument function")
    #function with one argument
    def mloading_fun(self,a):
        print("one argument function")
    #function with two argument
    def mloading_fun(self,a,b):
        print("two argument function")
mloadobj = methodoverloading()
mloadobj.mloading_fun(10,20)

print("Note ::--- method overloading is not support in pyhton because python is interpreter language")
            

        
