"""
# 100. Same Tree (Easy)
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# NeetCode 150 / Blind 75: Trees

Example 1:
    Input: p = [1,2,3], q = [1,2,3]
    Output: true

Example 2:
    Input: p = [1,2], q = [1,null,2]
    Output: false

Example 3:
    Input: p = [1,2,1], q = [1,1,2]
    Output: false

Approach: Recursive DFS
- If both nodes are None, they are the same.
- If one is None and the other is not, they differ.
- If values differ, they are not the same.
- Recurse on left and right subtrees.

Time Complexity:  O(n) — visit each node once
Space Complexity: O(h) — recursion stack, h = height of the tree (O(log n) balanced, O(n) skewed)
"""

from __future__ import annotations


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    """Return True if two binary trees are structurally identical with the same node values."""
    # Base cases
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    # Check current node values and recurse on children
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


# ── Inline Tests ──────────────────────────────────────────────────────────────

def _build_tree(values: list[int | None]) -> TreeNode | None:
    """Build a binary tree from a level-order list (None for missing nodes)."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def _test_same_tree():
    # Both empty trees
    assert is_same_tree(None, None) is True

    # Both single-node identical
    assert is_same_tree(TreeNode(1), TreeNode(1)) is True

    # Different single-node values
    assert is_same_tree(TreeNode(1), TreeNode(2)) is False

    # One None, one not
    assert is_same_tree(None, TreeNode(1)) is False
    assert is_same_tree(TreeNode(1), None) is False

    # Example 1: [1,2,3] vs [1,2,3] → True
    p = _build_tree([1, 2, 3])
    q = _build_tree([1, 2, 3])
    assert is_same_tree(p, q) is True

    # Example 2: [1,2] vs [1,None,2] → False
    p = _build_tree([1, 2])
    q = _build_tree([1, None, 2])
    assert is_same_tree(p, q) is False

    # Example 3: [1,2,1] vs [1,1,2] → False
    p = _build_tree([1, 2, 1])
    q = _build_tree([1, 1, 2])
    assert is_same_tree(p, q) is False

    # Larger identical trees
    p = _build_tree([1, 2, 3, 4, 5, 6, 7])
    q = _build_tree([1, 2, 3, 4, 5, 6, 7])
    assert is_same_tree(p, q) is True

    # Larger trees, one differing deep node
    p = _build_tree([1, 2, 3, 4, 5, 6, 7])
    q = _build_tree([1, 2, 3, 4, 5, 6, 8])
    assert is_same_tree(p, q) is False

    print("All Same Tree tests passed!")


if __name__ == "__main__":
    _test_same_tree()
