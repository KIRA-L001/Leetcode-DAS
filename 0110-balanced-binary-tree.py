from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(n):
            if not n: return 0
            l = height(n.left); r = height(n.right)
            if l == -1 or r == -1 or abs(l - r) > 1: return -1
            return 1 + max(l, r)
        return height(root) != -1

# refreshed 20260909-100055
