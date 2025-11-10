#finally block in exception

print("--->> finally block <<----")

try:
    print("hello")
    #print(x) here also finally block is executed
except:
    print("something went wrong")
finally:
    print("finally block")
