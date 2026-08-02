"""
146. LRU Cache (Medium)

Problem:
    Design a data structure that follows the constraints of a Least Recently
    Used (LRU) cache.

    Implement the LRUCache class:
      - LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
      - int get(int key) Return the value of the key if the key exists, otherwise return -1.
      - void put(int key, int value) Update the value of the key if the key exists.
        Otherwise, add the key-value pair to the cache. If the number of keys exceeds
        the capacity from this operation, evict the least recently used key.

    Follow up: Could you do get and put in O(1) time complexity?

Approach:
    Hash map + doubly linked list.
    - The hash map provides O(1) lookup by key.
    - The doubly linked list maintains access order: most recently used at the
      head, least recently used at the tail.
    - On get(): move the accessed node to the head.
    - On put(): if key exists, update and move to head; if new and at capacity,
      evict the tail node, then insert at head.

Time Complexity:  O(1) for both get and put
Space Complexity: O(capacity)

Example:
    >>> cache = LRUCache(2)
    >>> cache.put(1, 1)
    >>> cache.put(2, 2)
    >>> cache.get(1)
    1
    >>> cache.put(3, 3)   # evicts key 2
    >>> cache.get(2)
    -1
    >>> cache.put(4, 4)   # evicts key 1
    >>> cache.get(1)
    -1
    >>> cache.get(3)
    3
    >>> cache.get(4)
    4
"""


class _Node:
    """Doubly linked list node."""

    __slots__ = ("key", "value", "prev", "next")

    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev: _Node | None = None
        self.next: _Node | None = None


class LRUCache:
    """LRU Cache with O(1) get and put operations."""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: dict[int, _Node] = {}
        # Sentinel head and tail to avoid None checks
        self.head = _Node()
        self.tail = _Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: _Node) -> None:
        """Detach a node from the linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node: _Node) -> None:
        """Insert a node right after the sentinel head."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _move_to_head(self, node: _Node) -> None:
        """Move an existing node to the head (most recently used)."""
        self._remove(node)
        self._add_to_head(node)

    def _pop_tail(self) -> _Node:
        """Remove and return the least recently used node (before sentinel tail)."""
        lru = self.tail.prev
        assert lru is not None  # sentinel guarantees this
        self._remove(lru)
        return lru

    def get(self, key: int) -> int:
        """Return the value if key exists, else -1."""
        node = self.cache.get(key)
        if node is None:
            return -1
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """Insert or update the key-value pair, evicting LRU if over capacity."""
        node = self.cache.get(key)
        if node is not None:
            # Key exists — update value and move to head
            node.value = value
            self._move_to_head(node)
        else:
            # New key — create node and add to head
            new_node = _Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)

            if len(self.cache) > self.capacity:
                # Evict the least recently used node
                lru = self._pop_tail()
                del self.cache[lru.key]


if __name__ == "__main__":
    # Inline tests
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1, "Test 1 failed"
    cache.put(3, 3)  # evicts key 2
    assert cache.get(2) == -1, "Test 2 failed"
    cache.put(4, 4)  # evicts key 1
    assert cache.get(1) == -1, "Test 3 failed"
    assert cache.get(3) == 3, "Test 4 failed"
    assert cache.get(4) == 4, "Test 5 failed"

    # Edge case: capacity 1
    cache2 = LRUCache(1)
    cache2.put(1, 1)
    assert cache2.get(1) == 1
    cache2.put(2, 2)  # evicts key 1
    assert cache2.get(1) == -1
    assert cache2.get(2) == 2

    # Update existing key
    cache3 = LRUCache(2)
    cache3.put(1, 1)
    cache3.put(2, 2)
    cache3.put(1, 10)  # update key 1
    assert cache3.get(1) == 10, "Update test failed"
    assert cache3.get(2) == 2, "Key 2 should still exist"

    print("All LRU Cache tests passed.")
