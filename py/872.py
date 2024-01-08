# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.getLeaves(root1) == self.getLeaves(root2)

    def getLeaves(self, root: Optional[TreeNode]) -> list:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        return self.getLeaves(root.left) + self.getLeaves(root.right)

# Time: O(n), Space: O(n)
