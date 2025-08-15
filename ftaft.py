def max_points(c, k):
    n = len(c)
    left_sum = sum(c[:k])      
    right_sum = 0
    max_total = left_sum      
    for i in range(1, k + 1):
        left_sum -= c[k - i]         
        right_sum += c[-i]          
        max_total = max(max_total, left_sum + right_sum)

    return max_total

# Example
c = [1, 2, 3, 4, 5, 6, 1]
k = 3
print(max_points(c, k))