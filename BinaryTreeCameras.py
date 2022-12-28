from typing import Optional

from TreeNode import TreeNode


def minCameraCover(root: Optional[TreeNode]) -> int:

    cameras = 0
    # 0 means need to be covered, 1 means has a camera, 2 means been covered
    def helper(node):
        nonlocal cameras
        if not node:
            return 2
        left = helper(node.left)
        right = helper(node.right)

        if left == 0 or right == 0:
            cameras += 1
            return 1
        if left == 1 or right == 1:
            return 2
        return 0

    if helper(root) == 0:
        cameras += 1
    return cameras




