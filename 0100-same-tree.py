"""
100. Same Tree (Easy)

Problem:
    Given the roots of two binary trees p and q, write a function to check
    if they are structurally identical and have the same node values.

Approach:
    Recursive depth-first comparison. Two trees are the same if:
    1. Both roots are None, OR
    2. Both roots exist and have same value and same left and right subtrees.

Complexity:
    Time:  O(n) where n is the number of nodes in the smaller tree.
    Space: O(h) where h is the height of the tree (recursion stack).
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p, q):
    """Check if two binary trees are identical."""
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


if __name__ == "__main__":
    # Test 1: Both empty
    assert is_same_tree(None, None) == True
    
    # Test 2: Same tree
    #     1
    #    / \
    #   2   3
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    assert is_same_tree(p, q) == True
    
    # Test 3: Different structure
    #     1         1
    #    /          \
    #   2            2
    p2 = TreeNode(1, TreeNode(2))
    q2 = TreeNode(1, None, TreeNode(2))
    assert is_same_tree(p2, q2) == False
    
    print("All tests passed for 0100-same-tree")