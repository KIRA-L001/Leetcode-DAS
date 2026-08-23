from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        out = []
        def dfs(n, path):
            if not n: return
            path += str(n.val)
            if not n.left and not n.right: out.append(path)
            else:
                path += '->'
                dfs(n.left, path); dfs(n.right, path)
        dfs(root, '')
        return out

# refreshed 20260823-123438
