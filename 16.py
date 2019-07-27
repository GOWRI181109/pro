gow=int(input())
lak=list(map(int,input().split()))
dd=[1]*gow
for i in range(gow):
    if i==0:
        if lak[i]>lak[i+1]:
            dd[i]=dd[i]+dd[i+1]
    elif i>0:
        if lak[i]>lak[i-1]:
            dd[i]=dd[i]+dd[i-1]
print(sum(dd))
