arr=list(map(int,input().split()))
s=0
for i in range(len(arr)):
    if i%2!=0 and arr[i]%2==0:
        s=s+arr[i]
print(s)
