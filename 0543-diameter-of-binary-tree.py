"""
LeetCode 543. Diameter of Binary Tree (Easy)

Problem:
    Given the root of a binary tree, return the diameter — the number
    of edges on the longest path between any two nodes.

Approach:
    Post-order DFS. For each node, the longest path through it is
    depth(left) + depth(right). Track the global max while returning
    1 + max(child depths) upward.

Complexity:
    Time:  O(n)
    Space: O(h) recursion stack.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter_of_binary_tree(root):
    """Return the diameter (edge count of the longest path)."""
    best = 0

    def depth(node):
        nonlocal best
        if node is None:
            return 0
        left = depth(node.left)
        right = depth(node.right)
        best = max(best, left + right)
        return 1 + max(left, right)

    depth(root)
    return best


def build(values):
    """Build a tree from a level-order list (None = missing node)."""
    if not values:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


if __name__ == "__main__":
    assert diameter_of_binary_tree(build([1, 2, 3, 4, 5])) == 3  # 4-2-1-3
    assert diameter_of_binary_tree(build([1, 2])) == 1
    assert diameter_of_binary_tree(build([1])) == 0
    assert diameter_of_binary_tree(None) == 0
    print("All tests passed for LeetCode 543.")
