class ListNode:
    def __init__(self, val=0, next=None): self.val = val; self.next = next
class Solution:
    def reorderList(self, head) -> None:
        if not head or not head.next: return
        slow = fast = head
        while fast and fast.next: slow = slow.next; fast = fast.next.next
        prev = None; cur = slow
        while cur: nxt = cur.next; cur.next = prev; prev = cur; cur = nxt
        p, q = head, prev
        while q:
            p.next, p = q, p.next
            q.next, q = p, q.next

# refreshed 20260825-123515
