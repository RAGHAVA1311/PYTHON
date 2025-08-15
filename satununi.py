# finding kth largest element in an array 
# finding smallest element in an array
# finding largest element in an array
# cod e to find kth largest element in an array is
def kth_largest(arr, k):
     arr.sort()
     return arr[-k]
 
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
print(kth_largest(arr, k))

# code to find smallest element in an array is
def smallest(arr):
    arr.sort()
    return arr[0]

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(smallest(arr))

# code to find largest element in an array is
def largest(arr):
    arr.sort()
    return arr[-1]

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(largest(arr))
kth_largest(arr, k)


for i in range(1, 11):
    for j in range(1, 11):
        if i == j:
            print(i, j)
        else:
            print(i, j)

