from typing import List


def countNegatives(grid: List[List[int]]) -> int:
    count = j = 0
    i = len(grid) - 1

    while i >= 0:
        j = 0
        while j < len(grid[0]) and grid[i][j] >= 0:
            j += 1
        count += len(grid[0]) - j
        i -= 1
    return count


if __name__ == '__main__':
    print(countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]) == 8)
