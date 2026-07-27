"""
101. Symmetric Tree
Given the root of a binary tree, check whether it is a mirror of itself (symmetric).

Approach: Recursively compare left subtree with mirrored right subtree.
Time: O(n)  Space: O(h) recursion depth.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: Optional[TreeNode]) -> bool:
    def mirror(a, b):
        if not a and not b:
            return True
        if not a or not b or a.val != b.val:
            return False
        return mirror(a.left, b.right) and mirror(a.right, b.left)
    return mirror(root, root)

if __name__ == "__main__":
    t = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
    assert isSymmetric(t) is True
    t2 = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
    assert isSymmetric(t2) is False
    assert isSymmetric(None) is True
    print("0101 OK")
