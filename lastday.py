def can_make_amount(coins, amount):
    n = len(coins)
    dp = [[0] * (amount + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1  # Amount 0 is always possible (use no coins)

    for i in range(1, n + 1):
        for j in range(1, amount + 1):
            if coins[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i][j - coins[i - 1]]

    return bool(dp[n][amount]), dp[n]  # Return if we can make the amount and the DP table

# Example
coins = [2, 3, 5]
amount = 11
can_make, table = can_make_amount(coins, amount)
print("Can we make amount 11?", can_make)


 

