"""
509. Fibonacci Number
Return the nth Fibonacci number.

Approach: DP with O(1) space (two vars).
Time: O(n)  Space: O(1)
"""
def fib(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(10) == 55
    print("0509 OK")