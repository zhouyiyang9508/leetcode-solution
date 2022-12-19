from typing import List


def combine(n: int, k: int) -> List[List[int]]:
    def dfs(start, curr):
        # meets the length k
        if len(curr) == k:
            # use[:] to create a copy
            output.append(curr[:])
            return

        for i in range(start, n + 1):
            curr.append(i)
            dfs(i + 1, curr)
            curr.pop()
    output = []
    # start from 1 to n
    dfs(1, [])
    return output


if __name__ == '__main__':
    print(combine(4, 2))
