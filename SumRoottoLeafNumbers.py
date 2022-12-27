from typing import Optional

from TreeNode import TreeNode


def sumNumbers(root: Optional[TreeNode]) -> int:

    total = 0
    def helper(node, temp):
        nonlocal total
        if not node:
            return
        temp = temp * 10 + node.val
        # leaf node
        if not node.left and not node.right:
            total += temp

        helper(node.left, temp)
        helper(node.right, temp)

    helper(root, 0)
    return total
