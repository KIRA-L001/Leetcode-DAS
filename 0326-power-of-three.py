"""
326. Power of Three
Return True if n is a power of three.
Approach: Divide by 3 while divisible, check if we reach 1.
Time: O(log_3 n)  Space: O(1)
"""
def isPowerOfThree(n):
    if n < 1: return False
    while n % 3 == 0:
        n //= 3
    return n == 1
if __name__ == "__main__":
    assert isPowerOfThree(27) is True
    assert isPowerOfThree(0) is False
    print("0326 OK")
