 # search function in regular expression

import re

string = ("hi how are you ? all ohk  ")
a=re.search("\s",string)

print("the search of whitespace in string is : ",a.start())
