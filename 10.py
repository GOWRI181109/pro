gow=int(input())
bjk=[int(i) for i in input().split()]
xek=0
for k in range(gow):
   for j in range(k):
      if bjk[j]<bjk[k]:
         xek+=bjk[j]
print(xek) 
