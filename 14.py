gow,ri=map(int,input().split())
list1=list(map(int,input().split()))
gow=[]
list1.insert(0,0)
for y in range(ri):
     lan=[]
     s=0
     xx,yy=map(int,input().split())
     for i in range(xx,yy+1):         
         s^=list1[i]     
     gow.append(s)
for y in gow:
     print(y)
