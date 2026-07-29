"""
338. Counting Bits
Given n, return array ans where ans[i] = count of 1 bits in i's binary representation.

Approach: Dynamic programming using the observation ans[i] = ans[i >> 1] + (i & 1).
Time: O(n)  Space: O(n)
"""
from typing import List

def countBits(n: int) -> List[int]:
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i >> 1] + (i & 1)
    return ans

if __name__ == "__main__":
    assert countBits(5) == [0,1,1,2,1,2]
    assert countBits(2) == [0,1,1]
    print("0338 OK")