from typing import List


def removeDuplicates(nums: List[int]) -> int:
    slow, fast = 0, 1
    while fast < len(nums):
        if nums[slow] == nums[fast]:
            fast += 1
        else:
            nums[slow + 1], nums[fast] = nums[fast], nums[slow + 1]
            slow += 1
            fast += 1

    return slow + 1

