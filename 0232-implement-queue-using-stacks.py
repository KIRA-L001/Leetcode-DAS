class MyQueue:
    def __init__(self): self.s = []
    def push(self, x: int) -> None: self.s.append(x)
    def pop(self) -> int: return self.s.pop(0)
    def peek(self) -> int: return self.s[0]
    def empty(self) -> bool: return not self.s

# refreshed 20260828-142333
