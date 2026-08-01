"""
LeetCode #141 - Linked List Cycle
Difficulty: Easy
NeetCode 150 / Blind 75

Given the head of a linked list, determine if the list has a cycle in it.

A cycle exists if there is a node in the list that can be reached again by
continuously following the next pointer. Internally, pos is used to denote
the index of the node that tail's next pointer connects to (0-indexed).
Note that pos is not passed as a parameter.

Approach: Floyd's Tortoise and Hare (fast/slow pointer)
- Slow pointer moves one step at a time.
- Fast pointer moves two steps at a time.
- If there is a cycle, the fast pointer will eventually meet the slow pointer.
- If there is no cycle, the fast pointer will reach the end (None).

Time Complexity: O(n) where n is the number of nodes.
Space Complexity: O(1) only two pointers are used.
"""


class ListNode:
    """Definition for singly-linked list node."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def has_cycle(head: ListNode | None) -> bool:
    """Return True if the linked list has a cycle, False otherwise.

    >>> # No cycle: 1 -> 2 -> 3 -> None
    >>> n1 = ListNode(1)
    >>> n2 = ListNode(2)
    >>> n3 = ListNode(3)
    >>> n1.next = n2
    >>> n2.next = n3
    >>> has_cycle(n1)
    False

    >>> # Cycle: 1 -> 2 -> 3 -> back to 2
    >>> n1 = ListNode(1)
    >>> n2 = ListNode(2)
    >>> n3 = ListNode(3)
    >>> n1.next = n2
    >>> n2.next = n3
    >>> n3.next = n2  # cycle
    >>> has_cycle(n1)
    True

    >>> # Empty list
    >>> has_cycle(None)
    False

    >>> # Single node, no cycle
    >>> has_cycle(ListNode(1))
    False

    >>> # Single node pointing to itself (cycle)
    >>> n1 = ListNode(1)
    >>> n1.next = n1
    >>> has_cycle(n1)
    True
    """
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False


def has_cycle_set(head: ListNode | None) -> bool:
    """Alternative approach using a hash set to track visited nodes.

    Time Complexity: O(n)
    Space Complexity: O(n)

    >>> n1 = ListNode(1)
    >>> n2 = ListNode(2)
    >>> n1.next = n2
    >>> n2.next = n1  # cycle
    >>> has_cycle_set(n1)
    True

    >>> has_cycle_set(None)
    False
    """
    visited = set()
    current = head
    while current is not None:
        if current in visited:
            return True
        visited.add(current)
        current = current.next
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

    # Additional manual tests
    print("\n--- Manual Tests ---")

    # Test 1: No cycle
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n1.next = n2
    n2.next = n3
    assert has_cycle(n1) is False, "Test 1 failed"
    print("Test 1 passed: No cycle detected correctly")

    # Test 2: Cycle exists
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n1.next = n2
    n2.next = n3
    n3.next = n2  # cycle back to n2
    assert has_cycle(n1) is True, "Test 2 failed"
    print("Test 2 passed: Cycle detected correctly")

    # Test 3: Empty list
    assert has_cycle(None) is False, "Test 3 failed"
    print("Test 3 passed: Empty list handled correctly")

    # Test 4: Self-loop
    n1 = ListNode(1)
    n1.next = n1
    assert has_cycle(n1) is True, "Test 4 failed"
    print("Test 4 passed: Self-loop detected correctly")

    # Test 5: Large list no cycle
    head = ListNode(0)
    current = head
    for i in range(1, 10001):
        current.next = ListNode(i)
        current = current.next
    assert has_cycle(head) is False, "Test 5 failed"
    print("Test 5 passed: Large acyclic list handled correctly")

    # Test 6: Large list with cycle at the end
    head = ListNode(0)
    current = head
    nodes = [head]
    for i in range(1, 10001):
        current.next = ListNode(i)
        current = current.next
        nodes.append(current)
    current.next = nodes[5000]  # create cycle
    assert has_cycle(head) is True, "Test 6 failed"
    print("Test 6 passed: Large cyclic list detected correctly")

    print("\nAll tests passed!")
