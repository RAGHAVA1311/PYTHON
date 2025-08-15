def fun(arr,i=0,res=[]):
    if i==len(arr):
        print(res,end=" ")
        return
    fun(arr,i+1,res+[arr[i]])
    fun(arr,i+1,res)

arr=[1,2,3]
fun(arr)

def fun(arr,i,k):
    if k==0:
        return True
    if i==0:
        return False
    if arr[i-1]==k:
        return True
    return fun(arr,i-1,k-arr[i-1]) 

arr=[1,2,3]
k=4
n=len(arr)
if fun(arr,n,k):
    print("YES")
else:
    print("NO")
        