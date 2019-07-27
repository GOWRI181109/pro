gow1=int(input())
gow2=list(map(int,input().split()))
hkt=0
for x in range(len(gow2)-2):
    for y in range(x+1,len(gow2)-1):
        for z in range(y+1,len(gow2)):
            if gow2[x]<gow2[y]<gow2[z] and x<y<z:
                hkt=hkt+1
print(hkt)
