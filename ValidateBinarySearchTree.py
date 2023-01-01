import collections
from typing import Optional

from TreeNode import TreeNode


def isValidBST(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    stack = collections.deque()
    curr, prev = root, float('-inf')
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        if curr.val <= prev:
            return False
        prev = curr.val
        curr = curr.right
    return True

