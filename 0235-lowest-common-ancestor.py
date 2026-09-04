from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right
class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p, q) -> Optional[TreeNode]:
        while root:
            if root.val < p.val and root.val < q.val: root = root.right
            elif root.val > p.val and root.val > q.val: root = root.left
            else: return root
        return None

# refreshed 20260904-154618
