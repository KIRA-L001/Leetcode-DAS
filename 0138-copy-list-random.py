class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = x; self.next = next; self.random = random
class Solution:
    def copyRandomList(self, head: Optional['Node']) -> Optional['Node']:
        if not head: return None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = Node(cur.val, nxt)
            cur = nxt
        cur = head
        while cur:
            if cur.random: cur.next.random = cur.random.next
            cur = cur.next.next
        new_head = head.next; p = head
        while p:
            q = p.next; p.next = q.next
            if q.next: q.next = q.next.next
            p = q.next
        return new_head

# refreshed 20260830-230832
