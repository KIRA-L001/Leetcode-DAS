from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        cur = root
        while cur:
            if cur.left:
                prev = cur.left
                while prev.right: prev = prev.right
                prev.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right

# refreshed 20260828-112805
