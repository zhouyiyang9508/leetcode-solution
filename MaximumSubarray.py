from typing import List


def maxSubArray(nums: List[int]) -> int:
    max_sum = nums[0]
    curr_sum = nums[0]

    for n in nums[1:]:
        curr_sum = max(n, curr_sum + n)
        max_sum = max(max_sum, curr_sum)

    return max_sum


if __name__ == '__main__':
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6)