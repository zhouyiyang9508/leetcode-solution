import collections
from typing import Optional, List

from TreeNode import TreeNode


def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    queue = collections.deque()
    queue.append(root)
    output = []
    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if i == size - 1:
                output.append(node.val)

    return output


