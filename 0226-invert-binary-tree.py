"""
LeetCode 226. Invert Binary Tree (Easy)

Problem:
    Given the root of a binary tree, invert the tree (mirror it) and
    return its root.

Approach:
    Recursive DFS — swap the left and right children of every node,
    then recurse into the (already swapped) subtrees.

Complexity:
    Time:  O(n)  — every node visited once.
    Space: O(h) — recursion stack, h = tree height (O(n) worst case).
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    """Return the root of the mirrored tree."""
    if root is None:
        return None
    # Swap children, then invert each subtree.
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


def to_list(root):
    """Level-order serialization (Nones trimmed) for easy assertions."""
    out, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


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
    assert to_list(invert_tree(build([4, 2, 7, 1, 3, 6, 9]))) == [4, 7, 2, 9, 6, 3, 1]
    assert to_list(invert_tree(build([2, 1, 3]))) == [2, 3, 1]
    assert invert_tree(None) is None
    print("All tests passed for LeetCode 226.")
