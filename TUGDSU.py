def lemonadeChange(bills):
    five,ten=0,0 
    for c in bills:
        if c==5:
            five+=1
        elif c==10:
            if five>0:
                five-=1
                ten+=1,ValueError
            else:
                return False
        elif c==20:
            if ten>0 and five>0:
                ten-=1
                five-=1
            elif five>=3:
                five-=3
            else:
                return False
    return True
# Test cases
bills = list(map(int, input().split()))
print(lemonadeChange(bills))