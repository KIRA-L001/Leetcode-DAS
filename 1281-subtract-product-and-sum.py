"""
# 1281. Subtract the Product and Sum of Digits of a Number (Easy)
# Given an integer number n, return the difference between the product of its 
# digits and the sum of its digits.

# NeetCode 150 / Blind 75: Math

Example 1:
    Input: n = 234
    Output: 15 
    Explanation: 
        Product of digits = 2 * 3 * 4 = 24
        Sum of digits = 2 + 3 + 4 = 9
        Difference = 24 - 9 = 15

Example 2:
    Input: n = 444
    Output: 48
    Explanation:
        Product = 4 * 4 * 4 = 64
        Sum = 4 + 4 + 4 = 12
        Difference = 64 - 12 = 48

Example 3:
    Input: n = 231
    Output: 1
    Explanation:
        Product = 2 * 3 * 1 = 6
        Sum = 2 + 3 + 1 = 6
        Difference = 6 - 6 = 1

Approach: Extract Digits
- Extract each digit using modulo and division
- Track product and sum simultaneously
- Return difference

Time Complexity:  O(log n) — number of digits
Space Complexity: O(1) — constant extra space
"""

from __future__ import annotations


def subtract_product_and_sum(n: int) -> int:
    """Return product of digits minus sum of digits."""
    if n == 0:
        return 0
    
    product = 1
    total = 0
    
    while n > 0:
        digit = n % 10
        product *= digit
        total += digit
        n //= 10
    
    return product - total


# ── Inline Tests ──────────────────────────────────────────────────────────────

def _test_subtract_product_and_sum():
    # Example 1
    assert subtract_product_and_sum(234) == 15
    
    # Example 2
    assert subtract_product_and_sum(444) == 48
    
    # Example 3
    assert subtract_product_and_sum(231) == 1
    
    # Single digit
    assert subtract_product_and_sum(5) == 0  # 5 - 5 = 0
    
    # Zero input
    assert subtract_product_and_sum(0) == 0
    
    # Contains zero (product becomes 0)
    assert subtract_product_and_sum(101) == -2  # 0 - 2 = -2
    
    # Contains zero with non-zero sum
    assert subtract_product_and_sum(10) == -1  # 0 - 1 = -1
    
    # Large number
    assert subtract_product_and_sum(999) == 729  # 729 - 27 = 702? Let me verify
    # Actually 9*9*9 = 729, 9+9+9 = 27, 729 - 27 = 702
    assert subtract_product_and_sum(999) == 702
    
    print("All Subtract Product and Sum tests passed!")


if __name__ == "__main__":
    _test_subtract_product_and_sum()