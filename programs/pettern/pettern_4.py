# * * * * (r=1 ,c=1-4 , star =4 ,space = 0 )
#   * * * * ( r= 2, c=2-5,star = 4 space = 1)
#    * * * * ( r= 3, c=3-6,star = 4 space = 2)
#     * * * * ( r= 4, c=4-7,star = 4 space = 3)
#      * * * * ( r= 5, c=5-8,star = 4 space = 4)

print("the input pettern: ")
print(" * * * *",
"\n  * * * *",
"\n   * * * *",
"\n     * * * *",
"\n      * * * *")

print("the output pettern: ")

for r in range(1,6):
    for s in range(r):
        print(" " ,end="")
    for c in range(1,4):
        print("*",end=" ")
    print("*")
    
        
        

    

    
    



