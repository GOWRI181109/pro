gowz=int(input())
s=[]
for i in range(0,gowz):
 tin=input()
 s.append(tin)
wan=[]
for i in zip(*s):
 if(i.count(i[0])==len(i)):
  wan.append(i[0])
 else:
  break
print(''.join(wan))
