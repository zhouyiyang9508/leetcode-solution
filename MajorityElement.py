from typing import List


def majorityElement(nums: List[int]) -> int:
    count = 0
    candidate = 0
    for i in range(len(nums)):
        if count == 0:
            candidate = nums[0]
        count += (1 if candidate == nums[i] else - 1)
    return candidate


if __name__ == '__main__':
    print(majorityElement([2,2,1,1,1,2,2]) == 2)

