import collections
from typing import List


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    seen = [[0 for _ in range(n)] for _ in range(m)]
    maxArea = 0

    for i in range(m):
        for j in range(n):
            # find not seen 1
            if grid[i][j] and not seen[i][j]:
                shape = 0
                stack = collections.deque()
                stack.append((i, j))
                seen[i][j] = 1
                while stack:
                    r, c = stack.pop()
                    shape += 1
                    # dfs in 4 directions to find adjacent 1s
                    for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] and not seen[nr][nc]:
                            stack.append((nr, nc))
                            seen[nr][nc] = 1

                # after stack is empty, calculate the max
                maxArea = max(maxArea, shape)

    return maxArea

if __name__ == '__main__':
    print(maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
