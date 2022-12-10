from typing import Optional

import TreeNode


def maxProduct(self, root: Optional[TreeNode]) -> int:
    total_sum = []

    def calc_total_sum(node):
        if not node:
            return 0
        left = calc_total_sum(node.left)
        right = calc_total_sum(node.right)
        curr_sum = left + right + node.val
        total_sum.append(curr_sum)
        return curr_sum

    root_sum = calc_total_sum(root)
    maximum = 0
    for s in total_sum:
        maximum = max(maximum, (root_sum - s) * s)
    return maximum
