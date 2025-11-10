#elif_condition_statement

print("--->> elif condition statement <<----")
a =input("enter the value of a : ")
b = input("enter the value of b : ")
c =input("enter the value of c : ")

print("a =",a)
print("b =",b)
print("c =",c)

if a> b and a > c:
    print("a is greter than")
elif b > c:
    print("b is greter than")
else:
    print("c is greter than")

