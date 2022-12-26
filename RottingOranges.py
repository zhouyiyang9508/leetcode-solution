import collections
from typing import List


def orangesRotting(grid: List[List[int]]) -> int:
    queue = collections.deque()
    numFresh = 0
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j))
            elif grid[i][j] == 1:
                numFresh += 1

    minutes = 0
    while queue and numFresh > 0:
        size = len(queue)
        minutes += 1
        for _ in range(size):
            i, j = queue.popleft()
            for r, c in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                    queue.append((r, c))
                    numFresh -= 1
                    # turn fresh to rotten
                    grid[r][c] = 2

    return minutes if numFresh == 0 else -1

if __name__ == '__main__':
    print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))