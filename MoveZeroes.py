from typing import List


def moveZeroes(nums: List[int]) -> None:
    left, right = 0, 0
    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1
    print(nums)

if __name__ == '__main__':
    moveZeroes([0,1,0,3,12])
