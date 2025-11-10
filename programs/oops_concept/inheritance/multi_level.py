#multilevel inheritance

print("--->> Multilevel inheritance <<---\n ")

class grand_parent_class:
    def grand_parent_fun(self):
        print("i am grand parent class function ")
class parent_class(grand_parent_class):
    def parent_class_fun(self):
        print("i am parent class function: ")
class child_class(parent_class):
    def child_class_fun(self):
        print("i am child class function: ")


multilevelobj = child_class()
print("after create object of child class is multilevelobj  ")
print("--->> call a grand parent class function ")
print("grand parent class fun is : ",end="")
multilevelobj.grand_parent_fun()

print("--->> call a parent class function ")
print("parent class fun is : ",end="")
multilevelobj.parent_class_fun()


print("--->> call a child class function ")
print("child class fun is : ",end="")
multilevelobj.child_class_fun()
