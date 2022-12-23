from typing import List


def canJump(nums: List[int]) -> bool:
    last_position = len(nums) - 1
    for i in range(last_position - 1, -1, -1):
        if nums[i] + i >= last_position:
            last_position = i

    return last_position == 0

if __name__ == '__main__':
    print(canJump([2,3,1,1,4]))