#list store in file

print("--->> list store in file <<-----")
l1=["i am coming from list_into_file ","python","java","c","c++"]
print(" Note :---- the list is store in single quote in file because its store in a single block memory")
print("my list is : ", l1)
file=open("py_demo2.txt","w")
file.writelines(l1)
print("file is created :")
file.close()
print("\n")

#read a list from file

print("--->> Read list from file <<-----")
file=open("py_demo2.txt","r")
filelist=file.readlines()
print("list is coming from file py_demo2.txt : " ,filelist  )
