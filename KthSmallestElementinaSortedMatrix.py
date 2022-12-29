from typing import List


def kthSmallest(matrix: List[List[int]], k: int) -> int:
    n = len(matrix)
    left, right = matrix[0][0], matrix[n - 1][n - 1]
    while left < right:
        mid = (right + left) // 2
        # count elements <= middle row by row
        count = 0
        for i in range(n):
            j = n - 1
            while j >= 0 and matrix[i][j] > mid:
                j -= 1
            count += (j + 1)
        # kth on the left side
        if count >= k:
            right = mid
        else:
            left = mid + 1
    return left

if __name__ == '__main__':
    print(kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))

