from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        def dfs(n):
            if not n: return
            out.append(n.val); dfs(n.left); dfs(n.right)
        dfs(root)
        return out
