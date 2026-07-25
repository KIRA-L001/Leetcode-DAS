"""
21. Merge Two Sorted Lists (Easy)

Problem:
    Merge two sorted singly linked lists and return the head of the merged
    sorted list.

Approach:
    Iterative merge with a dummy head. Repeatedly attach the smaller of the
    two current nodes, then append whichever list remains.

Complexity:
    Time:  O(n + m) - each node visited once.
    Space: O(1) - pointers only, nodes are reused.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 or l2  # attach the leftover list
    return dummy.next


def build(values):
    """Helper: build a linked list from a Python list."""
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(node):
    """Helper: convert a linked list back to a Python list."""
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


if __name__ == "__main__":
    assert to_list(merge_two_lists(build([1, 2, 4]), build([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert to_list(merge_two_lists(build([]), build([]))) == []
    assert to_list(merge_two_lists(build([]), build([0]))) == [0]
    print("All tests passed for 0021-merge-two-sorted-lists")
