from typing import List


def pivotIndex(nums: List[int]) -> int:
    s = sum(nums)
    left_sum = 0
    for i in range(len(nums)):
        if left_sum == s - nums[i] - left_sum:
            return i
        left_sum += nums[i]
    return -1


if __name__ == '__main__':
    print(pivotIndex([1,7,3,6,5,6]))