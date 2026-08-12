"""
LeetCode #86 - Partition List
Difficulty: Medium
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head, x: int):
        less = ListNode(0)
        greater = ListNode(0)
        l, g = less, greater
        while head:
            if head.val < x:
                l.next = head
                l = l.next
            else:
                g.next = head
                g = g.next
            head = head.next
        g.next = None
        l.next = greater.next
        return less.next
