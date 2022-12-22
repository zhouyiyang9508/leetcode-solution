from typing import Optional

from TreeNode import TreeNode


def flatten(root: Optional[TreeNode]) -> None:

    def helper(node):
        if not node:
            return None
        # leaf node
        if not node.left and not node.right:
            return node

        left_tail = helper(node.left)
        right_tail = helper(node.right)

        # if left subtree is not empty
        if left_tail:
            left_tail.right = node.right
            node.right = node.left
            node.left = None

        # return rightmost node in the left subtree
        return right_tail if right_tail else left_tail

    return helper(root)