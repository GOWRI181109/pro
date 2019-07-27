gow,ri=map(int,input().split())
last=list(map(int,input().split()))
lkl=[]
for i in range(0,ri):
     x,y=map(int,input().split())
     lkl.append([x,y])
for i in range(ri):
     lower=lkl[i][0]
     upper=lkl[i][1]
     lan=sum(last[lower-1:upper])
     print(lan)
