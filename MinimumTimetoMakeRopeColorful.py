from typing import List


def minCost(colors: str, neededTime: List[int]) -> int:
    totalCost = 0
    i, j = 0, 0
    while j < len(neededTime):
        currMax = 0
        currTotal = 0

        # find group
        while j < len(neededTime) and colors[i] == colors[j]:
            currTotal += neededTime[j]
            currMax = max(currMax, neededTime[j])
            j += 1

        totalCost += currTotal - currMax
        i = j
    return totalCost

if __name__ == '__main__':
    print(minCost('abaac', [1,2,3,4,5]))