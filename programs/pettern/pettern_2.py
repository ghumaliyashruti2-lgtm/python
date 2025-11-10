#* * * * *(r=1,c=5)
#* * * *(r=2,c=4)
#* * *(r=3,c=3)
#* *(r=2,c=2)
#*(r=1,c=1)

print("the input pettern: ")
print("* * * * *","\n* * * *","\n* * *","\n* *","\n*",)

print("the output pettern: ")
for r in range(1,6):
    for c in range(5,r,-1):
        print("*",end=" ")
    r=r+1
    print("*")

    
    



