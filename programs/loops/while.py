#while loop

print("--->> while loop <<----")
sum = 0
n = int(input("enter the range of loop : "))
print("your loop range is : ",n)

while n > 0:
    sum = sum +n
    print(sum)
    n=n-1
    if n>0:
        print(n,"+",sum,"=",end=" ")
print("Your sum is : " , sum)

