l=list(map(int,input().split()))
max=0
sun=0
for i in l:
    if i>max:
        sun+=1
        max=i
print(sun)
