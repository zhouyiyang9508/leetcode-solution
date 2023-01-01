import collections
from typing import List


def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    queue = collections.deque()

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                mat[i][j] = -1
            else:
                queue.append((i, j))

    while queue:
        i, j = queue.popleft()
        for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= ni < m and 0 <= nj < n and mat[ni][nj] == -1:
                queue.append((ni, nj))
                mat[ni][nj] = mat[i][j] + 1

    return mat


if __name__ == '__main__':
    print(updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
    print(updateMatrix([[[0,0,0],[0,1,0],[0,0,0]]]))

