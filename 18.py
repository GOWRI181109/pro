gow,kum=map(int,input().split())
mah=[]
hkj=0
for i in range(gow):
    mah.append(list(map(int,input().split())))   
for i in range(gow):
    for j in range(kum-1):
        for k in range(j+1,kum+1):
            if mah[i][j:k]==[1]*len(mah[i][j:k]):
                 if all(mah[p+i][j:k]==[1]*len(mah[p+i][j:k]) for p in range(len(mah[i][j:k])-1)):
                     if len(mah[i][j:k])>hjk:
                        hjk=len(mah[i][j:k])
if len(mah)==1 and len(mah[0])==1 and mah[0][0]==1:
    print(1)
for i in range(hkj):
    print(*[1]*hkj)
