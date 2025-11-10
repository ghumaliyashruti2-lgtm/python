#hierarchical inheritance

print("--->> hierarchical inheritance <<---\n ")

class parent_class:
    def parent_class_fun(self):
        print("i am parent class function ")
class child1_class(parent_class):
    def child1_class_fun(self):
        print("i am child1 class function: ")
class child2_class(parent_class):
    def child2_class_fun(self):
        print("i am child2 class function: ")

print("--->> hierarchical inheritance create 2 object child1 and child2 ")

# child1 class object
hierarchicalchild1obj = child1_class()
print("--->> after create object of hietarchicalchild1obj  ")
print("--->> call a parent class function ")
print("parent class fun is : ",end="")
hierarchicalchild1obj.parent_class_fun()


# child2 class object
hierarchicalchild2obj =child2_class()
print("--->> after create object of hietarchicalchild2obj  ")
print("--->> call a parent class function ")
print("parent class fun is : ",end="")
hierarchicalchild2obj.parent_class_fun()

print("------------ Note:: ----------- \n Basically both child class object is called a parent class attribute and self class ")


