#change the by object

print("--->> change the value by object <<-----\n")

class changevalue_byobject_class:
    def __init__(self,name,age):
        self.name =  name
        self.age = age
chngvalueobj = changevalue_byobject_class("shreya",22)

print("--->> value is access from constructer")
print("the age is given by user is : ",chngvalueobj.age)
print("the name is given by user is : ",chngvalueobj.name)


#change my value using object

print("--->> value is change by object")
chngvalueobj.age = 34
print("the updated age of user is: ",chngvalueobj.age)
