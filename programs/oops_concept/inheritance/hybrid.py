#hybrid inheritance

print("--->> Hybrid inheritance <<---\n ")

class parent_class:
    def parent_class_fun(self):
        print("i am parent class function ")
class child1_class(parent_class):
    def child1_class_fun(self):
        print("i am child1 class function ")
class child2_class(parent_class):
    def child2_class_fun(self):
        print("i am child2 class function ")
class child3_class(child1_class,child2_class):
    def child3_class_fun(self):
        print("i am child3 class function ")
        

print("[[[ Hybrid inheritance create multiple object child1 and child2 and child3 \ni] child1 class object access a property of parent class and it self\nii] child2 class object access a property of parent class and it self\niii] child3 class object access a property of all class parent child1 child2 and it self ]]]\n")

# child1 class object
hybridchild1obj = child1_class()
print("--->> after create object of hybridchild1obj  ")
print("-> call a parent class function :-",end="")
hybridchild1obj.parent_class_fun()


# child2 class object
hybridchild2obj =child2_class()
print("\n--->> after create object of hybridchild2obj  ")
print("-> call a parent class function :-",end="")

hybridchild2obj.parent_class_fun()

#child3 class object
hybridchild3obj = child3_class()
print("\n--->> after create object of hybridchild3obj call all class functions <<------ \n ")
print("-> call a parent class function :-",end="")
hybridchild3obj.parent_class_fun()

print("\n-> call a child1 class function :-",end="")
hybridchild3obj.child1_class_fun()

print("\n-> call a child2 class function :-",end="")
hybridchild3obj.child2_class_fun()

print("\n-> call a self class function :-",end="")
hybridchild3obj.child3_class_fun()


