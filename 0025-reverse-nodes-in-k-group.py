
"""
LeetCode #25 - Reverse Nodes in k-Group
Difficulty: Hard
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while True:
            curr = prev
            for _ in range(k):
                curr = curr.next
                if not curr:
                    return dummy.next
            nxt = curr.next
            a, b = prev.next, curr
            for _ in range(k):
                tmp = a.next
                a.next = b.next
                b.next = a
                b = a
                a = tmp
            tmp = prev.next
            prev.next = b
            prev = tmp
        return dummy.next
