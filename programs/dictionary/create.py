# create dictionary

print("--->> create dictionary <<----")
d1 = {1: "ppple", 2: "mango", 3: "orange", 4:"cherry", 'a':'b'}
print("My dictionary is :",d1)
print("type of dictionary is: ",type(d1))

#store multiple values on key value (using list )

print("--->> store multiple values on key value (using list ) <<----")
d2 = {1:"python" ,2: "java" ,"fruit":["apple","banana","kiwi","cherry"]}
print("My multiple value stored dictionary is :",d2)
print("type of dictionary is: ",type(d2))


#store multiple values on key value (using tuple)

print("--->> store multiple values on key value (using tuple) <<----")
d3 = {1:"python" ,2: "java" ,"language":("java","python","c","c++")}
print("My multiple value stored dictionary is :",d3)
print("type of dictionary is: ",type(d3))


#Access the value of dict

print("--->> Access the value of dict <<----")
d1 = {1: "ppple", 2: "mango", 3: "orange", 4:"cherry", 'a':'b'}
print("My dictionary is :",d1)
x= d1[4]
print("access value of dictionary is : ",x)
