"""
102. Binary Tree Level Order Traversal
Given the root of a binary tree, return the level order traversal (left-to-right, level by level).

Approach: BFS with a queue, processing one full level per iteration.
Time: O(n)  Space: O(w) where w = max width of the tree.
"""
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    res, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res

if __name__ == "__main__":
    t = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert levelOrder(t) == [[3], [9, 20], [15, 7]]
    assert levelOrder(None) == []
    print("0102 OK")
