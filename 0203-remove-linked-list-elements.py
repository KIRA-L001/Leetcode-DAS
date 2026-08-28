class ListNode:
    def __init__(self, val=0, next=None): self.val = val; self.next = next
class Solution:
    def removeElements(self, head, val: int):
        dummy = ListNode(0, head); cur = dummy
        while cur.next:
            if cur.next.val == val: cur.next = cur.next.next
            else: cur = cur.next
        return dummy.next

# refreshed 20260828-112805
