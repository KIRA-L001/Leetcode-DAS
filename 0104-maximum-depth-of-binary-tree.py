"""
LeetCode 104. Maximum Depth of Binary Tree (Easy)

Problem:
    Given the root of a binary tree, return its maximum depth: the number of
    nodes along the longest path from root to a leaf.

Approach:
    Simple recursion: depth(node) = 1 + max(depth(left), depth(right)),
    with an empty tree having depth 0.

Complexity:
    Time:  O(n) - every node visited once.
    Space: O(h) - recursion stack, h = tree height.
"""


class TreeNode:
    """Binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    """Return the maximum depth of the binary tree rooted at root."""
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


if __name__ == "__main__":
    # Tree: [3, 9, 20, None, None, 15, 7] -> depth 3
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_depth(root) == 3
    # Tree: [1, None, 2] -> depth 2
    assert max_depth(TreeNode(1, None, TreeNode(2))) == 2
    assert max_depth(None) == 0
    assert max_depth(TreeNode(1)) == 1
    print("All tests passed for 0104-maximum-depth-of-binary-tree")
