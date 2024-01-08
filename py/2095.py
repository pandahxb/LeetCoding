from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current, middle = head, head
        if head.next is None:
            head = None
            return head
        current = head.next
        while current.next is not None:
            current = current.next
            if current.next is not None:
                current = current.next
                middle = middle.next
        middle.next = middle.next.next
        return head

# Time: O(n), Space: O(1)
