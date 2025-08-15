def fun(n,sum):
    if n<1:
        print(sum)
        return
    fun(n-1,sum+n)
n =9 
fun(n,0)
