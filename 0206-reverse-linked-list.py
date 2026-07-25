"""
206. Reverse Linked List (Easy)

Problem:
    Reverse a singly linked list and return the new head.

Approach:
    Iterative pointer reversal: walk the list keeping a `prev` pointer and
    flip each node's `next` to point backwards.

Complexity:
    Time:  O(n)
    Space: O(1)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    prev = None
    while head:
        nxt = head.next   # save forward link
        head.next = prev  # reverse pointer
        prev = head
        head = nxt
    return prev


def build(values):
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


if __name__ == "__main__":
    assert to_list(reverse_list(build([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert to_list(reverse_list(build([1, 2]))) == [2, 1]
    assert to_list(reverse_list(build([]))) == []
    print("All tests passed for 0206-reverse-linked-list")
