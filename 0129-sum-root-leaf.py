from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        def dfs(n, cur):
            nonlocal total
            if not n: return
            cur = cur * 10 + n.val
            if not n.left and not n.right: total += cur
            dfs(n.left, cur); dfs(n.right, cur)
        dfs(root, 0)
        return total

# refreshed 20260822-140033
