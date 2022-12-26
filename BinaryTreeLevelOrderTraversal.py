import collections
from typing import Optional, List

from TreeNode import TreeNode


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    level, res = 0, []
    queue = collections.deque()
    queue.append(root)

    while queue:
        res.append([])
        for i in range(len(queue)):
            node = queue.popleft()
            res[level].append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1

    return res
