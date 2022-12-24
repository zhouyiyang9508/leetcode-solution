from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    left, right = 0, len(nums) - 1
    result = [0] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            temp = nums[left]
            left += 1
        else:
            temp = nums[right]
            right -= 1
        result[i] = temp * temp

    return result

if __name__ == '__main__':
    print(sortedSquares([-4,-1,0,3,10]))
