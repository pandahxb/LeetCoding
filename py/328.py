# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        current = head
        second = head.next
        odd = True
        while current.next.next is not None:
            next = current.next
            current.next = next.next
            current = next
            odd = not odd
        if odd:
            current.next = second
        else:
            current.next.next = second
            current.next = None
        return head

# Time: O(n), Space: O(1)
