from typing import Optional
class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val; self.left = left; self.right = right; self.next = next
class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root: return None
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next: head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        return root

# refreshed 20260821-102507
