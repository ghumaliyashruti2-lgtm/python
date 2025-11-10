#how to create a class

print("--->> create a class  <<-----")
class myclass:
    x=5
    print("the value of x in class : ", x)
#print(myclass)# error occured because of class cant access without object.


#how to create a obejct
print("--->> create a object  <<-----")
class object_class:
    x=5
obj=object_class()
print("The value of x is access by obj: ",obj.x)
