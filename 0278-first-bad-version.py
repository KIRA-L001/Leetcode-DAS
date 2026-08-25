class Solution:
    def firstBadVersion(self, n: int, isBad=None) -> int:
        lo, hi = 1, n
        while lo < hi:
            mid = (lo+hi)//2
            if isBad(mid): hi = mid
            else: lo = mid+1
        return lo

# refreshed 20260825-123515
