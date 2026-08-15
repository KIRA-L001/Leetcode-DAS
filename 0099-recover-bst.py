"""
LeetCode #99 - Recover Binary Search Tree
Difficulty: Hard
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first = second = prev = None
        def dfs(node):
            nonlocal first, second, prev
            if not node:
                return
            dfs(node.left)
            if prev and node.val < prev.val:
                if not first:
                    first = prev
                second = node
            prev = node
            dfs(node.right)
        dfs(root)
        first.val, second.val = second.val, first.val
