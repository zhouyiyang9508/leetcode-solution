from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    m, n = len(board), len(board[0])

    def dfs(i, j, start):
        if start == len(word):
            return True
        if word[start] != board[i][j]:
            return False

        for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= ni < m and 0 <= nj < n:
                if dfs(ni, nj, start + 1):
                    return True

        return False

    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0):
                return True
    return False

if __name__ == '__main__':
    print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCCED'))

