from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        out = []
        def dfs(n):
            if not n: return
            dfs(n.left); out.append(n.val); dfs(n.right)
        dfs(root)
        return out[k-1]
