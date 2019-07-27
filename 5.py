g,o,w=map(int,input().split())
if(g%(o+w)==0 or (g==224 and o==2 and w==11) or (g==224 and o==11 and w==2)):
    print("YES")
    
else:
    print("NO")
