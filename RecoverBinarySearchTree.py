import collections
from typing import Optional

from TreeNode import TreeNode


def recoverTree(root: Optional[TreeNode]) -> None:
    x = y = prev = None
    stack = collections.deque()

    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if prev:
            if prev.val > root.val:
                y = root
                if x is None:
                    x = prev
                else:
                    break
        prev = root
        root = root.right

    x.val, y.val = y.val, x.val