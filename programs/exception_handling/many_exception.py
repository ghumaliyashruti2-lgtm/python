# handle multiple exception 

print("--->> handle multiple exception <<-----")
try:    
    print(x)
except NameError:
    print("variable is not defined")
except:
    print("exception occured")
