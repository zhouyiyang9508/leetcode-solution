from collections import Counter
from typing import Optional, List

from TreeNode import TreeNode


def findFrequentTreeSum(root: Optional[TreeNode]) -> List[int]:
    maxFreq = 0
    counter = Counter()

    def helper(node):
        nonlocal maxFreq
        if not node:
            return 0
        left = helper(node.left)
        right = helper(node.right)

        tempSum = left + right + node.val
        counter[tempSum] += 1
        if counter[tempSum] > maxFreq:
            maxFreq = counter[tempSum]
        return tempSum

    helper(root)

    res = []
    for val, freq in counter:
        if freq == maxFreq:
            res.append(val)

    return res

