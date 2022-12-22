from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    # fill with different coins
    for coin in coins:
        # amount smaller than coin will ask for at least one coin
        for i in range(coin, amount + 1):
            # pick this coin or skip
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == '__main__':
    print(coinChange([1,2,5], 11))
    print(coinChange([2], 3))


