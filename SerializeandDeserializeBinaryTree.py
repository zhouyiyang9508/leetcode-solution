import collections

from TreeNode import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        queue = collections.deque()
        res = ""
        queue.append(root)
        while queue:
            node = queue.popleft()
            if not node:
                res += "None,"
            res += str(node.val) + ","
            queue.append(node.left)
            queue.append(node.right)
        return res


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        strs = data.split(",")
        queue = collections.deque()
        root = TreeNode(int(strs[0]))
        queue.append(root)
        index = 1
        while queue and index < len(strs):
            node = queue.popleft()
            if strs[index] != "None":
                left = TreeNode(int(strs[index]))
                node.left = left
                queue.append(left)
            index += 1
            if strs[index] != "None":
                right = TreeNode(int(strs[index]))
                node.right = right
                queue.append(right)
            index += 1

        return root
