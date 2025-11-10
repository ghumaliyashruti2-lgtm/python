# for loop

print("--->> for loop <<----")
a = int(input("Enter the range number: "))
print("your range number is: ",a)
for i in range (a):
    print(a)
    a=a-1


b=["hi","good","morning","dear"]
#print(type(b))
print("your list is : ",b)
for i in (b):
    print(i,len(i))
print("------> Total character in word is <------")
for i in (b):
    print(i,"=",len(i))
