from typing import List


def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    min_price = prices[0]

    for p in prices[1:]:
        max_profit = max(max_profit, p - min_price)
        min_price = min(min_price, p)

    return max_profit

if __name__ == '__main__':
    print(maxProfit([7,1,5,3,6,4]) == 5)
