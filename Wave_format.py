n=int(input())
l=list(map(int,input().split()))
l.sort()
z=[]
while len(z)<n:
    if len(l)>=2:
        z.append(l[-2])
        z.append(l[-1])
        del l[-1]
        del l[-1]
    else:
        z.append(l[-1])
print(*z)
    