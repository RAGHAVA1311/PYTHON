n=int(input())
l=list(map(int, input().split()))
pol=0
crimes=0
for i in l:
    if i==-1:
        if pol>0:
            pol-=1
        else:
            crimes+=1
    else:
        pol+=i
print(crimes)
