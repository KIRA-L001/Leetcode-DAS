"""
LeetCode 2. Add Two Numbers (Medium)

Problem:
    Two non-empty linked lists represent two non-negative integers stored in
    reverse order (one digit per node). Add the two numbers and return the sum
    as a linked list, also in reverse order.

Approach:
    Traverse both lists simultaneously, adding digit pairs plus a running
    carry. Build the result list node by node with a dummy head.

Complexity:
    Time:  O(max(m, n)) - single pass over both lists.
    Space: O(max(m, n)) - the output list.
"""


class ListNode:
    """Simple singly-linked list node."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1, l2):
    """Return the linked list representing the sum of l1 and l2."""
    dummy = ListNode()
    current = dummy
    carry = 0
    while l1 or l2 or carry:
        total = carry
        if l1:
            total += l1.val
            l1 = l1.next
        if l2:
            total += l2.val
            l2 = l2.next
        carry, digit = divmod(total, 10)
        current.next = ListNode(digit)
        current = current.next
    return dummy.next


def _build(digits):
    """Build a linked list from a list of digits (least significant first)."""
    dummy = ListNode()
    cur = dummy
    for d in digits:
        cur.next = ListNode(d)
        cur = cur.next
    return dummy.next


def _to_list(node):
    """Convert a linked list back into a Python list of digits."""
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


if __name__ == "__main__":
    # 342 + 465 = 807
    assert _to_list(add_two_numbers(_build([2, 4, 3]), _build([5, 6, 4]))) == [7, 0, 8]
    # 0 + 0 = 0
    assert _to_list(add_two_numbers(_build([0]), _build([0]))) == [0]
    # 9999999 + 9999 = 10009998 (carry propagation)
    assert _to_list(
        add_two_numbers(_build([9] * 7), _build([9] * 4))
    ) == [8, 9, 9, 9, 0, 0, 0, 1]
    print("All tests passed for 0002-add-two-numbers")
