from typing import List


def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()
    minDiff, ans = float('inf'), float('inf')

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            temp = nums[i] + nums[left] + nums[right]
            if abs(temp - target) < minDiff:
                minDiff = abs(temp - target)
                ans = temp

            if temp > target:
                right -= 1
            elif temp == target:
                return target
            else:
                left += 1
    return ans

if __name__ == '__main__':
    print(threeSumClosest([-1,2,1,-4], 1))