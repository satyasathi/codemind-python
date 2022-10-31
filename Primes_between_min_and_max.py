from math import sqrt
def prime(n):
    if n==0 or n==1:
        return False
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True

n=int(input())
l=list(map(int,input().split()))
x=min(l)
x1=l.index(x)
y=max(l)
y1=l.index(y)
c=0
for i in range(n):
    if (i>=x1 and i<=y1) or (i>=y1 and i<=x1):
        if prime(l[i]):
            c+=1
print(c)