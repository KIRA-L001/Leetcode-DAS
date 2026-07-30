"""
876. Middle of the Linked List
Return the middle node (second middle if even).
Approach: Slow/fast pointers.
Time: O(n)  Space: O(1)
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next
def middleNode(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    assert middleNode(head).val == 3
    print("0876 OK")
