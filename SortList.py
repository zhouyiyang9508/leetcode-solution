from typing import Optional

from ListNode import ListNode


def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    def merge(left, right):
        dummy = ListNode(-1)
        curr = dummy
        while left and right:
            if left.val > right.val:
                curr.next = right
                right = right.next
            else:
                curr.next = left
                left = left.next
            curr = curr.next

        if left:
            curr.next = left
        if right:
            curr.next = right
        return dummy.next

    if not head or not head.next:
        return head

    # find middle element
    prev, slow, fast = None, head, head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # prev points to the last element of the first half part
    prev.next = None

    left = sortList(head)
    right = sortList(slow)

    return merge(left, right)


if __name__ == '__main__':
    n1 = ListNode(-1)
    n2 = ListNode(5)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(0)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    head = sortList(n1)
    while head:
        print(head.val)
        head = head.next