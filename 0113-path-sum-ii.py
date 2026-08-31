from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(n, s, path):
            if not n: return
            path.append(n.val)
            if not n.left and not n.right and s == n.val: res.append(path[:])
            dfs(n.left, s - n.val, path); dfs(n.right, s - n.val, path)
            path.pop()
        dfs(root, targetSum, [])
        return res

# refreshed 20260831-130836
