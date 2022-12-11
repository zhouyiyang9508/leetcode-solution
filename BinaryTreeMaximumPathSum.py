from typing import Optional

import TreeNode


def maxPathSum(self, root: Optional[TreeNode]) -> int:
    max_path = -float('inf')

    def calc_max_path(node):
        nonlocal max_path
        if not node:
            return 0

        left = max(0, calc_max_path(node.left))
        right = max(0, calc_max_path(node.right))

        # pick left + right + node as a path
        max_path = max(max_path, left + right + node.val)
        # pick left + node or right + node as a partial path
        return max(left + node.val, right + node.val) 

    calc_max_path(root)

    return max_path