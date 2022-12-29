from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    while left < right:
        mid = (left + right) // 2
        midElement = matrix[mid // n][mid % n]
        if midElement >= target:
            right = mid
        else:
            left = mid + 1
    return matrix[left // n][left % n] == target


if __name__ == '__main__':
    print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
    print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))