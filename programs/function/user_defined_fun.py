# user defined function

print("------>>> user defined function <<<------")

def myfunction():
    print("Hello , How Are you ?")
myfunction()


# function with one argument

def myfunction(x):
    print("---->> function with one argument <<<------ ")
    print("value of x : ", x)
myfunction(20)

# function with multiple argument

def myfunction(x,y,z):
    print("---->> function with multiple argument <<<------ ")
    print("value of x :",x)
    print("value of y :",y)
    print("value of z: ",z)
myfunction(10,20,30)


#keyword argument function
def myfunction(x,y):
    print("---->> function with keyword argument <<<----- ")
    print("x = ",x)
    print("y = ",y)
    
    if(x>y):
        print("value of x is greter than y  ")
    else:
        print("value of y is greter than x  ")
myfunction(x=2,y=5)


#default perameter value

print("---->> default perameter value function <<<------ ")
def myfunction(fruit="kiwi"):
    print("My favourate fruit is : ", fruit )
myfunction("apple")
myfunction("banana")
myfunction("orange")
myfunction("cherry")
myfunction()


#passing list into function

def myfunction(car):
    print("---->> passing list into function <<<------ ")
    for i in car:
        print(i)
a = ["BMW","venue","kiya"]
myfunction(a)

#return values from function

print("---->> return values from function <<<------ ")
def myfunction(x):
    print("5 * ",x,"=",end=" ")
    return 5*x
print(myfunction(2))
print(myfunction(3))
print(myfunction(4))


#recursion function

print("---->> recursion function <<----- ")
def myfunction(x):
    if(x == 1):
        return x;
    else:
        return (x*myfunction (x-1))
n= int(input("enter the number which you want to factorial : "))
print("factorial of given number is :", n ,"factorial : ",myfunction(n))

    
