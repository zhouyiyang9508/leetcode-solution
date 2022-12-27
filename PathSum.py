from typing import Optional

from TreeNode import TreeNode


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:

    def helper(node, temp):
        if not node:
            return False
        if not node.left and not node.right:
            return temp + node.val == targetSum

        left = helper(node.left, temp + node.val)
        right = helper(node.right, temp + node.val)
        return left or right

    return helper(root, 0)
