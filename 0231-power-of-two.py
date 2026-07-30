"""
231. Power of Two
Return True if n is a power of two.
Approach: Single bit check — n > 0 and (n & (n-1)) == 0.
Time: O(1)  Space: O(1)
"""
def isPowerOfTwo(n):
    return n > 0 and (n & (n-1)) == 0
if __name__ == "__main__":
    assert isPowerOfTwo(1) is True
    assert isPowerOfTwo(16) is True
    assert isPowerOfTwo(3) is False
    print("0231 OK")
