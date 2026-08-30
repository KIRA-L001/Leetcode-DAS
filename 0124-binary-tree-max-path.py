from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = float('-inf')
        def dfs(n):
            if not n: return 0
            l = max(0, dfs(n.left)); r = max(0, dfs(n.right))
            self.best = max(self.best, l + r + n.val)
            return max(l, r) + n.val
        dfs(root)
        return self.best

# refreshed 20260830-230832
