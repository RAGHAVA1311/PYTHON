# recursion

def p_i(cu, n):
    if cu > n:
        return
    print(cu, end=" ")
    p_i(cu + 1, n)
def p_d(cu):
    if cu == 0:
        return
    print(cu, end=" ") 
    p_d(cu - 1)
n=5
p_i(1, n)
p_d(n - 1)








