#calling a function by obejct

print("--->> calling a function by object  <<-----")
class funobj_class:
    def objfun(self):
        print("hi, how are you ?")
        
funobj=funobj_class()
print("The function of objfun() is access by funobj: ",end="")
funobj.objfun()
# error ocurred fun(self) is missing its complusry because of 
