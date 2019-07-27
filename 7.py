any=int(input())
rak=1
while(rak<=any and rak*2<=any):
    rak=rak*2
if(rak==any):
    print("0")
else:    
    print(any-rak)
