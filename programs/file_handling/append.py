#append the value into file

print("--->> append the value into file <<-----")
a = "\n hello , how are you everyone"
file=open("py_demo1.txt","a")
file.write(a)
print("the content is added in the file py_demo1.txt")
file.close()

