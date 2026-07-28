"""
LeetCode 234. Palindrome Linked List (Easy)

Problem:
    Given the head of a singly linked list, return True if it reads
    the same forwards and backwards.

Approach:
    1. Find the middle with slow/fast pointers.
    2. Reverse the second half in place.
    3. Compare the two halves node by node.

Complexity:
    Time:  O(n)
    Space: O(1) — in-place reversal, no extra list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome(head):
    """Return True if the linked list is a palindrome."""
    if head is None or head.next is None:
        return True

    # 1. Middle: slow ends at mid (second half start for even lengths).
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 2. Reverse second half.
    prev = None
    while slow:
        slow.next, prev, slow = prev, slow, slow.next

    # 3. Compare halves.
    left, right = head, prev
    while right:  # right half is <= left half in length
        if left.val != right.val:
            return False
        left, right = left.next, right.next
    return True


def build(values):
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


if __name__ == "__main__":
    assert is_palindrome(build([1, 2, 2, 1])) is True
    assert is_palindrome(build([1, 2])) is False
    assert is_palindrome(build([1, 2, 3, 2, 1])) is True
    assert is_palindrome(build([1])) is True
    assert is_palindrome(build([])) is True
    print("All tests passed for LeetCode 234.")
