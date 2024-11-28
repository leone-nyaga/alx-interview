def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to make the given total.

    Args:
        coins (list): List of available coin denominations.
        total (int): The total amount to make change for.

    Returns:
        int: The fewest number of coins needed to meet the total,
             or -1 if it's not possible to make the total with the given coins.
    """
    if total <= 0:
        return 0
    
    dp = [float('inf')] * (total + 1)
    
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[total] if dp[total] != float('inf') else -1

