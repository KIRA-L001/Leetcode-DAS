"""
110. Balanced Binary Tree (Easy)

Problem:
    Given the root of a binary tree, determine if it is height-balanced.
    A height-balanced binary tree is a tree where the left and right
    subtrees of every node differ in height by no more than 1.

Approach:
    Post-order traversal. For each node, compute the height of left and
    right subtrees. If any subtree is unbalanced, return False early.
    The tree is balanced if all nodes have balanced subtrees.

Complexity:
    Time:  O(n) - each node visited once.
    Space: O(h) - recursion stack depth equals tree height.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root):
    """Check if a binary tree is height-balanced."""
    def check_height(node):
        if not node:
            return 0, True
        
        left_height, left_balanced = check_height(node.left)
        if not left_balanced:
            return 0, False
        
        right_height, right_balanced = check_height(node.right)
        if not right_balanced:
            return 0, False
        
        height = 1 + max(left_height, right_height)
        balanced = abs(left_height - right_height) <= 1
        
        return height, balanced
    
    _, balanced = check_height(root)
    return balanced


if __name__ == "__main__":
    # Test 1: Empty tree is balanced
    assert is_balanced(None) == True
    
    # Test 2: Balanced tree
    #     3
    #    / \
    #   9  20
    #      / \
    #     15  7
    root2 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert is_balanced(root2) == True
    
    # Test 3: Unbalanced tree
    #     1
    #    /
    #   2
    #  /
    #  3
    root3 = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert is_balanced(root3) == False
    
    print("All tests passed for 0110-balanced-binary-tree")