#operator precedence


print("--->> operator precedence <<----")
a = 20
b = 10
c = 15
d = 5

x = (a+b)*c/d  #(20+10)*15/5 -> (30)*15/5 -> 30*3 -> 90 <- ans
print("x is :" , x)

y=((a+b)*c)/d #((20+10)*15) -> (30)*15/5 -> 30*3 -> 90 <- ans
print("y is :" , y)

z=a+(b*c)/d #20+(10*15)/5 -> 20+(150)/5 -> 20+30 -> 50 <- ans
print("z is :", z)
