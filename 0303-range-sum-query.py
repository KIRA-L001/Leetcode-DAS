class NumArray:
    def __init__(self, nums: list):
        self.pre = [0]
        for n in nums: self.pre.append(self.pre[-1] + n)
    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right+1] - self.pre[left]
