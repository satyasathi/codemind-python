from math import sqrt
a,b,c=map(int,input().split(" "))
s=(a+b+c)/2
x=(s)*(s-a)*(s-b)*(s-c)
y=sqrt(x)
print("{:.2f}".format(y))