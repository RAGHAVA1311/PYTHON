def palli(s):
    l = 0
    r = len(s)-1
    while l < r:
        if s[l]!= s[r]:
            return False
        l += 1 
        r -= 1
    return True
s= "abcccba"
if palli(s):
    print("Palindrome")
else:
    print("Not a Palindrome")