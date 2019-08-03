gow=int(input())
kum=list(map(int,input().split()))
ans=int(gow/2)
rj=kum[:ans]
mk=kum[ans::]
if ((sum(rj)//len(rj))==(sum(mk)//len(mk))):
    print("yes")
else:
    print("no")
