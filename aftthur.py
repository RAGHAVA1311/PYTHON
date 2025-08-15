s='aaabbc'
res=[]
count = 1
for i in range(1,len(s)):
    if i>0 and s[i]==s[i-1]:
        count+=1
    else:
        count=1
    if count==2:
        res.append(s[i])
print(res)
# Output: ['a', 'b']
# Test cases
s = 'aaabbc'