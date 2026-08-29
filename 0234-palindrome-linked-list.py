class ListNode:
    def __init__(self, val=0, next=None): self.val = val; self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        vals = []
        while head: vals.append(head.val); head = head.next
        return vals == vals[::-1]

# refreshed 20260829-204107
