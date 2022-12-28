from typing import List


def sortArray(nums: List[int]) -> List[int]:
    def merge(left, right):
        result = []
        while left and right:
            if left[0] < right[0]:
                result.append(left[0])
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)

        if left:
            result += left
        if right:
            result += right
        return result

    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = sortArray(nums[:mid])
    right = sortArray(nums[mid:])

    return merge(left, right)


if __name__ == '__main__':
    print(sortArray([5,2,3,1]))
    print(sortArray([5,1,1,2,0,0]))

