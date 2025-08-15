# def fibonacci(n, a, b):
#     current = a + b
#     print(a,end=" ")
#     if n <= 0:
#         return b
#     return fibonacci(n   - 1, b, cburrent)
# # Example usage:
# print(fibonacci(10, 0, 1)) 
# tabulation 
# optimization 
def fib(n):
    if n <= 2:
        return 1
    fib = [0] * (n + 1)
    fib[1] = 1
    fib[2] = 1
    for i in range(3, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]
# Example usage:

print(fib(10))  # Output: 55