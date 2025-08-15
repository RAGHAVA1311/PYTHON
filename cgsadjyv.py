l = [2,5,1,7,10]
k = 14
a,r,sum,m = 0,0,0,0
while r < len(l):
    sum += l[r]
    if sum < k:
        r += 1
    elif sum > k:
        sum -= l[a]
        a += 1
    else:
        m = max(m,r-a+1)
        r += 1
print(m)
