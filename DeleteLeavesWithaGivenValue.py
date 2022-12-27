from typing import Optional

from TreeNode import TreeNode


def removeLeafNodes(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

    def helper(node):
        if not node:
            return None
        node.left = helper(node.left)
        node.right = helper(node.right)

        # node becomes leaf node
        if not node.left and not node.right:
            return None if node.val == target else node
        else:
            return node

    return helper(root)