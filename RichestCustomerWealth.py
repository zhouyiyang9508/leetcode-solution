from typing import List


def maximumWealth(accounts: List[List[int]]) -> int:
    maxWealth = 0
    for i in range(len(accounts)):
        maxWealth = max(sum(accounts[i]), maxWealth)

    return maxWealth

if __name__ == '__main__':
    print(maximumWealth([[1,2,3],[3,2,1]]) == 6)