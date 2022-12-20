from typing import List


def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    counter = [0] * 102
    for n in nums:
        counter[n + 1] += 1

    for i in range(1, len(counter)):
        counter[i] += counter[i - 1]

    return [counter[num] for num in nums]


if __name__ == '__main__':
    print(smallerNumbersThanCurrent([8,1,2,2,3]))