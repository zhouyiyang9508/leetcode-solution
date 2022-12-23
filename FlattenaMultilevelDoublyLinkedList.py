import collections

from TreeNode import TreeNode

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
    stack = collections.deque()
    stack.append(head)
    dummy = Node(0, None, head, None)
    dummy.next = head
    prev = dummy
    while stack:
        curr = stack.pop()
        curr.prev = prev
        prev.next = curr

        if curr.next:
            # append next node to be popped after child node
            stack.append(curr.next)
        if curr.child:
            stack.append(curr.child)
            # flatten child node
            curr.child = None

        prev = curr

    dummy.next.prev = None
    return dummy.next
