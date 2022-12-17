from typing import List


def maxOperations(nums: List[int], k: int) -> int:
    nums = sorted(nums)
    left, right = 0, len(nums) - 1
    count = 0
    while left < right:
        res = nums[left] + nums[right]
        if res == k:
            count += 1
            left += 1
            right -= 1
        elif res > k:
            right -= 1
        else:
            left += 1

    return count


if __name__ == '__main__':
    print(maxOperations([1,2,3,4], 5))
