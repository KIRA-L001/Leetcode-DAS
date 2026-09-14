from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity; self.m = OrderedDict()
    def get(self, key: int) -> int:
        if key not in self.m: return -1
        self.m.move_to_end(key); return self.m[key]
    def put(self, key: int, value: int) -> None:
        if key in self.m: self.m.move_to_end(key)
        self.m[key] = value
        if len(self.m) > self.cap: self.m.popitem(last=False)

# refreshed 20260914-100026
