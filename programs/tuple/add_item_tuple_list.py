# convert into list

print("---->> tuple convert into list and add item and convert into tuple <<-----")
a = (1,2,3,4,5,6,7)
print("a tuple :" , a)
print("type of a tuple : ", type(a))

#convert tuple into list 

print("---->> convert tuple into list  <<----")
b=list(a)
print("my list value : ",b)
print("type of b list : ", type(b))


# add item in list

print("---->> add item in list <<----")
b[3]=8
print("add item in list: ",b )


#convert list into tuple

print("---->> convert updated list into tuple <<----")
c =tuple((b))
print("after add value and convert list to tuple: ",c)
print("type of c tuple : ", type(c))
