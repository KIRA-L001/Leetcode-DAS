from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right
class Solution:
    def removeNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None
        if key < root.val: root.left = self.removeNode(root.left, key)
        elif key > root.val: root.right = self.removeNode(root.right, key)
        else:
            if not root.left: return root.right
            if not root.right: return root.left
            m = root.right
            while m.left: m = m.left
            root.val = m.val
            root.right = self.removeNode(root.right, m.val)
        return root

# refreshed 20260825-123515
