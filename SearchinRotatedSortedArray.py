from typing import List


def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        # middle on the left side
        if nums[mid] > nums[right]:
            if nums[mid] > target >= nums[left]:
                right = mid
            else:
                left = mid + 1
        # middle on the right side
        else:
            if nums[mid] > target >= nums[left]:
                right = mid
            else:
                left = mid + 1

    return left if nums[left] == target else -1


if __name__ == '__main__':
    print(search([4,5,6,7,0,1,2], 0))
    print(search([4,5,6,7,0,1,2], 3))



