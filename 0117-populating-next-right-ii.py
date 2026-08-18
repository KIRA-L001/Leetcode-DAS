from typing import Optional
class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val; self.left = left; self.right = right; self.next = next
class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root: return root
        dummy = Node(0); prev = dummy; head = root
        while head:
            if head.left:
                prev.next = head.left; prev = prev.next
            if head.right:
                prev.next = head.right; prev = prev.next
            head = head.next
            if not head:
                head = dummy.next; dummy.next = None; prev = dummy
        return root
