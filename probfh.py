def fun(l,n):
    if l==n:
        print(l,end=" ")
        return 0
    else:
        print(l,end=" ")
        return fun(l+1,n)
fun(1,5)
