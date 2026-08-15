"""
LeetCode #95 - Unique Binary Search Trees II
Difficulty: Medium
"""
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        def build(lo, hi):
            if lo > hi:
                return [None]
            result = []
            for i in range(lo, hi + 1):
                left = build(lo, i - 1)
                right = build(i + 1, hi)
                for l in left:
                    for r in right:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        result.append(node)
            return result
        return build(1, n)
