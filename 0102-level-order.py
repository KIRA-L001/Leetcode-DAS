"""
LeetCode #102 - Binary Tree Level Order Traversal
Difficulty: Medium
"""
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result, queue = [], [root]
        while queue:
            level, nxt = [], []
            for node in queue:
                level.append(node.val)
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            result.append(level)
            queue = nxt
        return result
