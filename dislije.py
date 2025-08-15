n = int(input())
b = n * 1.67
b = int(b)
for i in range(b):
    if i==0:
        pass
    elif i==1:
        print(1)
    elif i%3==0:
        pass
    elif i>10:
        y = i%10
        if y%3!=0:
           print(i)
    else :
        print(i)