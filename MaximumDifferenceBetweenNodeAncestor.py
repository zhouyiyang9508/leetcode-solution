from typing import Optional

import TreeNode


def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
    def helper(node, cur_max, cur_min):
        if not node:
            return cur_max - cur_min
        cur_max = max(cur_max, node.val)
        cur_min = min(cur_min, node.val)
        left = helper(node.left, cur_max, cur_min)
        right = helper(node.right, cur_max, cur_min)

        return max(left, right)

    return helper(root, root.val, root.val)
