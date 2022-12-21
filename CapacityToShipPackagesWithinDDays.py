from typing import List


def shipWithinDays(weights: List[int], days: int) -> int:
    left, right = max(weights), sum(weights)

    while left < right:
        mid, need, curr = (left + right) // 2, 1, 0
        for w in weights:
            if curr + w > mid:
                need += 1
                curr = 0
            curr += w
            # capacity too small
        if need > days:
            left = mid + 1
        else:
            right = mid

    return left

if __name__ == '__main__':
    print(shipWithinDays([3,2,2,4,1,4], 3))