class MinStack:
    def __init__(self): self.s = []
    def push(self, val: int) -> None:
        m = val if not self.s else min(val, self.s[-1][1])
        self.s.append((val, m))
    def pop(self) -> None: self.s.pop()
    def top(self) -> int: return self.s[-1][0]
    def getMin(self) -> int: return self.s[-1][1]

# refreshed 20260821-102507
