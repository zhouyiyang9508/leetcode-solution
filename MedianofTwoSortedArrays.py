from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    m, n = len(nums1), len(nums2)
    if m > n:
        return findMedianSortedArrays(nums2, nums1)
    left, right = 0, m
    while left <= right:
        cut1 = (left + right) // 2
        cut2 = (m + n + 1) // 2 - cut1

        l1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
        l2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
        r1 = float('inf') if cut1 == m else nums1[cut1]
        r2 = float('inf') if cut2 == n else nums2[cut2]

        if l1 > r2:
            # too many elements on l1
            right = cut1 - 1
        elif l2 > r1:
            left = cut1 + 1
        else:
            if (m + n) % 2 == 0:
                return (max(l1, l2) + min(r1, r2)) / 2
            else:
                return max(l1, l2)
    return -1

if __name__ == '__main__':
    print(findMedianSortedArrays([1,3], [2]) == 2.0)
    print(findMedianSortedArrays([1,2], [3, 4]) == 2.5)

