from typing import List


def trap(height: List[int]) -> int:
    leftMax, rightMax = 0, 0
    left, right = 0, len(height) - 1
    ans = 0

    while left < right:
        if leftMax < height[left]:
            leftMax = height[left]
        if rightMax < height[right]:
            rightMax = height[right]
        # we have the highest right bound and a higher left bound, so we can for sure contain some water here
        if leftMax < rightMax:
            ans += leftMax - height[left]
            left += 1
        if rightMax <= leftMax:
            ans += rightMax - height[right]
            right -= 1

    return ans

if __name__ == '__main__':
    print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))