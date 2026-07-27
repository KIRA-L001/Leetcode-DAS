"""
198. House Robber
You cannot rob two adjacent houses. Maximize the total amount robbed.

Approach: DP with two states (rob / skip). At each house, best = max(rob this + skip prev, skip this).
Time: O(n)  Space: O(1) (rolling).
"""
from typing import List

def rob(nums: List[int]) -> int:
    prev_rob = prev_skip = 0
    for money in nums:
        rob_this = prev_skip + money
        skip_this = max(prev_rob, prev_skip)
        prev_rob, prev_skip = rob_this, skip_this
    return max(prev_rob, prev_skip)

if __name__ == "__main__":
    assert rob([1, 2, 3, 1]) == 4
    assert rob([2, 7, 9, 3, 1]) == 12
    assert rob([2, 1, 1, 2]) == 4
    print("0198 OK")
