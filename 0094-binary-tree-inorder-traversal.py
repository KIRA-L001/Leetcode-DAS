"""
94. Binary Tree Inorder Traversal
Given the root of a binary tree, return the inorder traversal (left, root, right).

Approach: Iterative using an explicit stack (avoids recursion overhead / stack limits).
Time: O(n)  Space: O(h) where h = tree height (stack depth).
"""
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    res, stack = [], []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res

if __name__ == "__main__":
    # build tree: 1 -> right 2 -> left 3  => [1,3,2]
    t = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
    assert inorderTraversal(t) == [1, 3, 2]
    assert inorderTraversal(None) == []
    assert inorderTraversal(TreeNode(5)) == [5]
    print("0094 OK")
