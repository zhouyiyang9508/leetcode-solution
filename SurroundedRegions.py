import collections
from typing import List


def solve(board: List[List[str]]) -> None:
    queue = collections.deque()
    m, n = len(board), len(board[0])
    for i in range(m):
        for j in range(n):
            if (i in [0, m - 1] or j in [0, n - 1]) and board[i][j] == 'O':
                queue.append((i, j))

    while queue:
        i, j = queue.popleft()
        if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
            board[i][j] = 'S'
            queue.extend([(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)])

    for i in range(m):
        for j in range(n):
            if board[i][j] == 'S':
                board[i][j] = 'O'
            elif board[i][j] == 'O':
                board[i][j] = 'X'
    print(board)

if __name__ == '__main__':
    solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
