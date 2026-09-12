class Solution:
    def deleteNode(self, node):
        if node and node.next:
            node.val = node.next.val
            node.next = node.next.next

# refreshed 20260912-100004
