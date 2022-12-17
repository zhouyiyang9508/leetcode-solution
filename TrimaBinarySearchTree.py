from typing import Optional

import TreeNode


def trimBST(root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:

    def trim(node, low, high):
        if not node:
            return None
        # answer must be left tree
        if node.val > high:
            return trim(node.left)
        if node.val < low:
            return trim(node.right)
        node.left = trim(node.left, low, high)
        node.right = trim(node.right, low, high)
        return node

    return trim(root, low, high)