from typing import List


def rotate(nums: List[int], k: int) -> None:
    def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    n = len(nums)
    k = k % n
    # for example 1234567
    # reverse whole array to be 7654321
    reverse(nums, 0, n - 1)
    # reverse first k elements to be 567-4321
    reverse(nums, 0, k - 1)
    # reverse the rest elements to be 567-1234, reverse successfully..
    reverse(nums, k, n - 1)

if __name__ == '__main__':
    print(rotate([1,2,3,4,5,6,7], 3))