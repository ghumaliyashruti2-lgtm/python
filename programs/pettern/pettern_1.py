#* (r=1,c=1)
#* *(r=2,c=2)
#* * *(r=3,c=3)
#* * * *(r=4,c=4)
#* * * * *(r=5,c=5)

print("the input pettern: ")
print("*","\n* *","\n* * *","\n* * * *","\n* * * * *")

print("the output pettern: ")
for r in range(0,5):
    for c in range(r):
        print("*", end=" ") # increment value of column and put * in top to bottom 
    r=r+1  # increment a value of row and put value row right to left
    print("*")

    

