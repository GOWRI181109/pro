gow,ri=map(str,input().split())
wave=0
if len(gow)>len(ri):
   gow,ri=ri,mak
i=0
while i<len(gow):
  wave+=(ord(ri[i])-ord(gow[i]))
  i+=1
for i in range(i,len(ri)):
  wave+=ord(ri[i])-ord('a')+1
print(wave)
