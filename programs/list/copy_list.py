#copy list

print("--->> extend/copy one list to another list <<----")
a = [1,2,3,4,5,6,7]
print("my list1 : ",a)

b=[8,9,10,11]
print("my list2 : ",b)

#extend list

a.extend(b)
print("my extend list2 into list1 : ",a)
