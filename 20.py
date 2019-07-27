vvg,lom=map(int,input().split())
vir=list(map(int,input().split()))
vir.sort()
vir.reverse()
s=lom
pin=0
for i in vir:
    if(s>=i):
        jkl=int(s/i)
        pen=pen+jkl
        s=s-jkl*i
    if s==0:
        break
if(s==0):
   print(pen)
else:
   print("it's not posiible to select coins in such a way that they sum upto",lom)
