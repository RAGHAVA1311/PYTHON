def prime(n, divisor=None):
    # Base cases
    if n <= 1:
        return False
    if divisor is None:
        divisor = n - 1
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    # Recursive call
    return prime(n, divisor - 1)

# Example usage
print(prime(5))  # True
print(prime(10)) # False




