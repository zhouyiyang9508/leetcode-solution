import math
from typing import List


def minEatingSpeed(piles: List[int], h: int) -> int:
    left, right = 1, max(piles)
    smallest = right
    while left < right:
        mid = (left + right) // 2
        # count how many hours to spend
        count = 0
        for p in piles:
            count += math.ceil(p / mid)
        # eat too slow
        if count > h:
            left = mid + 1
        else:
            right = mid
    return left

if __name__ == '__main__':
    print(minEatingSpeed([30,11,23,4,20], 5))
    print(minEatingSpeed([30,11,23,4,20], 6))
