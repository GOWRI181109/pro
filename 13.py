xx,yy=map(int,input().split())
gow=[]
kum=[]
dhar=[int(m) for m in input().split() ]
for i in range(0,yy):
    uu1,vv1=map(int,input().split())
    for j in range(uu1-1 ,vv1):
        kum.append(dhar[j])
    mah=sorted(kum)
    cab.append(min(kum))
    del kum[:]
for z in range(0,len(gow)):
print(gow[z])
