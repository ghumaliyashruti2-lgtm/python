# user defined exception

print("--->> user defined exception <<-----")
class myexception(Exception):
    pass

a = 10
if a<12:
    raise myexception("something went wrong")
else:
    print("yes true")
    
