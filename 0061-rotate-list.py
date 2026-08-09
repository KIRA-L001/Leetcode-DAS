"""
LeetCode #61 - Rotate List
Difficulty: Medium
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head, k: int):
        if not head or not head.next:
            return head
        tail = head
        n = 1
        while tail.next:
            tail = tail.next
            n += 1
        tail.next = head
        k = k % n
        for _ in range(n - k):
            tail = tail.next
        head = tail.next
        tail.next = None
        return head
