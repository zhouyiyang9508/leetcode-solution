from typing import List


def maxArea(height: List[int]) -> int:
    maxWater = 0
    left, right = 0, len(height) - 1
    while left < right:
        maxWater = max(maxWater, (right - left) * min(height[left], height[right]))
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return maxWater

if __name__ == '__main__':
    print(maxArea([1,8,6,2,5,4,8,3,7]))