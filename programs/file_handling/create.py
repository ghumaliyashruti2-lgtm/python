#file create

print("--->> create a file <<----")
a="i am program of file create from (create.py) "
file=open("py_demo1.txt","w")
file.write(a)
print("the name of py_demo1.txt file is created")
file.close()
