from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    output = []
    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            three_sum = nums[i] + nums[left] + nums[right]
            if three_sum > 0:
                right -= 1
            elif three_sum < 0:
                left += 1
            else:
                output.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

    return output

if __name__ == '__main__':
    print(threeSum([-1,0,1,2,-1,-4]))