gow,ri=input().split()
man=abs(len(gow)-len(ri))
for i in range(len(gow)):
  if len(ri)==1 and ri[i] in gow:
   break
  if gow[i]!=ri[i]:
   man+=1
print(man)
