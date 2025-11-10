# replace function in regular expression

import re

string = "hello everyone how are you ? and how was your day ?"
print("before replace string :- ",string)

replace = re.sub(r"hello","hy",string)
print("after replace string :- ",replace)



string = "Python is Most trending Programming Lungage  ?"
print("before replace string :- ",string)

replace = re.sub(r"[A-Z]","0",string)
print("after replace string :- ",replace)
