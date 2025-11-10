#use a try block to handle exception occured by devide by zero

print("--->> use a try block to handle exception occured by devide by zero <<-----")
try:    
    a=int(input("enter the value of a : "))
    b=int(input("enter the value of b : "))
    c=a/b
    print("Answer is : ",c)
except Exception as e:
    print("Exception is : ",e)
