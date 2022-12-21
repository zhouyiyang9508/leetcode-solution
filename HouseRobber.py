from typing import List


def rob(nums: List[int]) -> int:
    n = len(nums)
    rob_next = nums[n - 1]
    rob_next_next = 0

    for i in range(n - 2, -1, -1):
        curr = max(nums[i] + rob_next_next, rob_next)
        rob_next_next = rob_next
        rob_next = curr
    return rob_next

if __name__ == '__main__':
    print(rob([1,2,3,1]))