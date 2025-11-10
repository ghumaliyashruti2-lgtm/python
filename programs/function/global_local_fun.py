# global variable in function :- use in anywhere in program

print("---->>> global variable in function <<<------")
a = 5
def myfunction():
    global a
    print("global variable a : ",a)
    a = 10 # global variable a value change here 
myfunction()
print("outside of function value of a : ",a )


# local variable in function :- use in scope of code 

print("---->>> local variable in function <<<------")
def myfunction(x,y):
    print("x : ",x)
    print("y : ",y)
    sum = x + y
    return sum
print("the sum of given x and y is : " ,myfunction(5,6))
#print(x) # because of x is local variable 



