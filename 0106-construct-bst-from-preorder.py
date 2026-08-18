from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None
        root = TreeNode(preorder[0])
        for v in preorder[1:]:
            cur = root
            while True:
                if v < cur.val:
                    if cur.left is None: cur.left = TreeNode(v); break
                    cur = cur.left
                else:
                    if cur.right is None: cur.right = TreeNode(v); break
                    cur = cur.right
        return root
