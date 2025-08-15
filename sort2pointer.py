def sort(y):
    l = 0
    r = len(y)-1
    while l < r:
        if y[l] >= y[l+1]:
            return False
        l += 1
    return True
y = [1,2,3,4,5,6,7,8,9]
print(sort(y))