import math
gow,kum=map(int,input().split())
srk=[]
bbb=list(map(int,input().split()))
for i in range(0,kum):
    vin,sri=map(int,input().split())
    srk.append([vin,sri])
for i in srk:
    lan=i[0]-1
    wan=i[1]-1
    print(math.gcd(bbb[lan],bbb[wan]))
