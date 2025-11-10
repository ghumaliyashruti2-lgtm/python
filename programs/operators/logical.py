# logical operators

print("--->> logical operatos <<----")

# and operation
print("--->> and operators <<----")
a = 40
b = 45
c = 30
if a > b and a > c :
    print(a,"is greter than to", b," and", c )
elif  b > c :
    print(b,"is greter than to", a," and", c )
else:
    print(c,"is greter than to", a," and", b )

#or operation
print("--->> or operators <<----")
a = True
b = False
print(a ," or", b ,"=" , a or b )

#not operation
print("--->> not operators <<----")
a = True
print(a,"not operator is : ", not a)


    
