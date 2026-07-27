"""
238. Product of Array Except Self
Return array `ans` where ans[i] = product of all elements except nums[i]. No division; O(n).

Approach: Left pass (prefix products) then right pass (suffix products), combined in place.
Time: O(n)  Space: O(1) extra (output array excluded).
"""
from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [1] * n
    left = 1
    for i in range(n):
        ans[i] = left
        left *= nums[i]
    right = 1
    for i in range(n - 1, -1, -1):
        ans[i] *= right
        right *= nums[i]
    return ans

if __name__ == "__main__":
    assert productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    print("0238 OK")
