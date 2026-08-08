"""
111. Minimum Depth of Binary Tree (Easy)

Problem:
    Given the root of a binary tree, return its minimum depth. The minimum
    depth is the number of nodes along the shortest path from the root
    node down to the nearest leaf node.

Approach:
    BFS (level-order traversal) from root. The first leaf encountered
    gives the minimum depth. This is more efficient than DFS for shallow
    trees since we can stop early.

Complexity:
    Time:  O(n) - in worst case, we visit all nodes.
    Space: O(w) where w is the maximum width of the tree (queue size).
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_depth(root):
    """Return the minimum depth of a binary tree."""
    if not root:
        return 0
    
    from collections import deque
    queue = deque([(root, 1)])
    
    while queue:
        node, depth = queue.popleft()
        
        # If this is a leaf node, we found the minimum depth
        if not node.left and not node.right:
            return depth
        
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    
    return 0


if __name__ == "__main__":
    # Test 1: Empty tree
    assert min_depth(None) == 0
    
    # Test 2: Single node
    assert min_depth(TreeNode(1)) == 1
    
    # Test 3: Tree with minimum depth 2
    #     1
    #    / \
    #   2   3
    root3 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert min_depth(root3) == 2
    
    # Test 4: Left-skewed tree
    #     1
    #    /
    #   2
    #  /
    # 3
    root4 = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert min_depth(root4) == 3
    
    print("All tests passed for 0111-minimum-depth-of-binary-tree")