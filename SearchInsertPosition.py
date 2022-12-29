from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == '__main__':
    print(searchInsert([1,3,5,6], 7))
    print(searchInsert([1,3,5,6], 2))

