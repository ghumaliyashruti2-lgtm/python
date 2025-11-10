#single inheritance

print("---->> single inheritance <<-----\n")

class single_parent_class:
    def parent_fun(self):
        print("i am parent class function ")
class single_child_class(single_parent_class):
    def child_fun(self):
        print("i am child class function: ")

singleobj = single_child_class()
print("after create object of singleobj ")
print("--->> call a parent class function ")
print("parent class fun is : ",end="")
singleobj.parent_fun()

print("--->> call a child class function ")
print("child class fun is : ",end="")
singleobj.child_fun()
