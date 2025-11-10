#multiple inheritance

print("--->> Multiple inheritance <<---\n ")

class parent1_class:
    def parent1_class_fun(self):
        print("i am parent1 class function ")
class parent2_class:
    def parent2_class_fun(self):
        print("i am parent2 class function: ")
class child_class(parent1_class,parent2_class):
    def child_class_fun(self):
        print("i am child class function: ")


multipleobj = child_class()
print("after create object of multipleobj  ")
print("--->> call a parent1 class function ")
print("parent1 class fun is : ",end="")
multipleobj.parent1_class_fun()

print("--->> call a parent2 class function ")
print("parent2 class fun is : ",end="")
multipleobj.parent2_class_fun()


print("--->> call a child class function ")
print("child class fun is : ",end="")
multipleobj.child_class_fun()
