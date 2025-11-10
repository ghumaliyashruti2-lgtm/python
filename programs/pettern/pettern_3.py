#        *(r=1,c=5,star=1,space=6-1=5)
#      * *(r=2,c=4,star=2,space)
#    * * *
#  * * * *
#* * * * *

print("the input pettern: ")
print("        *",
"\n      * *",
"\n    * * *",
"\n  * * * *",
"\n* * * * *")

print("the output pettern: ")
n = 5  # number of rows
for r in range(1, n + 1):        
    for s in range(n - r):       
        print(" ", end=" ")      
    for c in range(r):           
        print("*", end=" ")      
    print() 

    



