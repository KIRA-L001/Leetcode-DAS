"""
344. Reverse String
Write a function that reverses a string. Input is a character array, modify in-place.

Approach: Two pointers swap from ends towards center.
Time: O(n/2)  Space: O(1)
"""
from typing import List

def reverseString(s: List[str]) -> None:
    l, r = 0, len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

if __name__ == "__main__":
    s = list("hello")
    reverseString(s)
    assert s == list("olleh")
    print("0344 OK")