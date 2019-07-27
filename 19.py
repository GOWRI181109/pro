gow=int(input())
kum=[]
mak=[]
for i in range(gow):
    kum.append(list(map(int,input().split())))
for k in kum:
    for num in k:
        mak.append(num)
mak.sort()
for i in mak:
    print(i,end=' ')
