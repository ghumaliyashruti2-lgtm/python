 # match function in regular expression

import re

pattern = r"^hi"
string = ("hi how are you ? all ohk  ")
a=re.match(pattern,string)

print("the match of string is : ",a)
