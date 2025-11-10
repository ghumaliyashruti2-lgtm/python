# delete a object

print("--->> delete a object <<-----\n")

class delobj_class:
    def __init__(self,age,name):
        self.age = age
        self.name = name
delobj=delobj_class(22,"diya")
print("the age is given by user is : ",delobj.age)
print("---->> delete object: -----")
del delobj.age
print("after delete a variable of age when we access name variable : ",end="")
print(delobj.name)
print("after delete a variable of age when we access its given a error: ",end="")
print(delobj.age)



