def frequency(arr,num):
    # frequency of a given number in an array using only recursion no loops
    if len(arr)==0:
        return 0
    if arr[0]==num:      
        return 1+frequency(arr[1:],num)
    else:
        return frequency(arr[1:],num)

def main(): # driver code
    arr=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
    num=1
    print(frequency(arr,num))
if __name__=="__main__":
    main()
