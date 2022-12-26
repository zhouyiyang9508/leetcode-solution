from typing import Optional

from TreeNode import TreeNode


def pruneTree(root: Optional[TreeNode]) -> Optional[TreeNode]:

    # find if the subtree contains 1
    def helper(node):
        if not node:
            return False
        left = helper(node.left)
        right = helper(node.right)
        # left subtree does not contain 1
        if not left:
            # prune left subtree
            node.left = None
        if not right:
            node.right = None

        return True if node.val == 1 else left or right

    # if contains 1, return root, else return None
    return root if helper(root) else None
