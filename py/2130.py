# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        current, middle = head, head
        while current is not None:
            current = current.next.next
            middle = middle.next
        first = None
        second = middle
        third = middle.next
        middle.next = None
        while third is not None:
            first = second
            second = third
            third = third.next
            second.next = first
        maxSum = 0
        left, right = head, second
        while right is not None:
            maxSum = max(maxSum, left.val + right.val)
            left = left.next
            right = right.next
        return maxSum

# Time: O(n), Space: O(1)
