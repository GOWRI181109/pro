gow,kum = input().split()
kum = int(kum)
falm = False
bjk = list(map(int,input().split()))
for i in range(len(bjk)):
    for j in range(len(bjk)):
        if bjk[i]+bjk[j] == kum:
            falm = True
print("yes" if falm else "no") 
