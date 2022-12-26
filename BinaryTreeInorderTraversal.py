import collections
from typing import Optional, List

from TreeNode import TreeNode


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    stack = collections.deque()
    res = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        temp = stack.pop()
        res.append(temp)
        root = root.right

    return res
