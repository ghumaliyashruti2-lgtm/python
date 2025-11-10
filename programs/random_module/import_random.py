#import random

import random
print("hi")

#choice function

print("----->>choice function <<-----")
from random import choice
c1 = [2,4,6,8]
print("list : ",c1)
print("Random number from the given list is : ",choice(c1))
print("\n")


#Randint function

print("----->>Randint function <<-----")
from random import randint
a =randint(10000,99999)
print("Random number from the Randint function : ",a)


#shuffle function(candy crush match candy )
print("----->>shuffle function <<-----")
from random import shuffle
x = ["apple","kiwi","orange"]
shuffle(x)
print(x)
