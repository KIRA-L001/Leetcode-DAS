"""
382. Linked List Random Node
Given a singly linked list, return a random node value where each node has
equal probability of being chosen.

Approach: Reservoir sampling — iterate through list, keep one element,
replace with probability 1/i for node i.
Time: O(n)  Space: O(1)
"""
import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        res = self.head.val
        curr = self.head.next
        i = 2
        while curr:
            if random.random() < 1 / i:
                res = curr.val
            curr = curr.next
            i += 1
        return res

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3)))
    sol = Solution(head)
    # Test multiple times to check distribution (not asserting exact)
    vals = [sol.getRandom() for _ in range(100)]
    assert all(1 <= v <= 3 for v in vals)
    print("0382 OK")