# nested if condition statement

print("--->> nested if condition statement <<----")
a =input("enter the value of a : ")
b = input("enter the value of b : ")
c =input("enter the value of c : ")

print("a =",a)
print("b =",b)
print("c =",c)

if a> b:
    if a > c:
        print("a is greter than")
elif c > b:
    print("c is greter than")
else:
    print("b is greter than")

