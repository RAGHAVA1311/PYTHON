# l = list(map(int, input().split()))   
# sum = 0
# for i in l:
#     sum += i
# print(sum)

l=[-1,-1,2,-1,-1,-1,-1,-1,-1,-1,-1,1]
n=0
a=[]
for i in range(len(l)-1):
    if l[i]==-1:
        n=n+1
    elif l[i+1]<0:
        a.append(n)
        n=0
print(a)
