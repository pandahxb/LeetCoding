# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        first = None
        second = head
        third = head.next
        head.next = None
        while third is not None:
            first = second
            second = third
            third = third.next
            second.next = first
        second.next = first
        return second

# Time: O(n), Space: O(1)
