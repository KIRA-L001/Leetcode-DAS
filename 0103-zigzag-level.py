"""
LeetCode #103 - Binary Tree Zigzag Level Order Traversal
Difficulty: Medium
"""
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result, queue, left_to_right = [], [root], True
        while queue:
            level, nxt = [], []
            for node in queue:
                level.append(node.val)
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            result.append(level if left_to_right else level[::-1])
            left_to_right = not left_to_right
            queue = nxt
        return result
