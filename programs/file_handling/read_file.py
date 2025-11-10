#read file (note : file must be available otherwise file not found error accured);

print("--->> read file <<---- ")
print("file must be available otherwise file not found error accured")
file=open("py_demo1.txt","r")
filecontent=file.read()
print("content in the file : " ,filecontent)
file.close()
