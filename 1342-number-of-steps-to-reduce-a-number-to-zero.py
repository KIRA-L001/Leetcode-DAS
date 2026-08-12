"""
# 1342. Number of Steps to Reduce a Number to Zero (Easy)
# Given a non-negative integer num, return the number of steps to reduce it to 0.
# - If the number is even, divide it by 2
# - If the number is odd, subtract 1 from it

# NeetCode 150 / Blind 75: Bit Manipulation

Example 1:
    Input: num = 14
    Output: 6
    Explanation: 
        step 1: 14 / 2 = 7
        step 2: 7 - 1 = 6
        step 3: 6 / 2 = 3
        step 4: 3 - 1 = 2
        step 5: 2 / 2 = 1
        step 6: 1 - 1 = 0

Example 2:
    Input: num = 8
    Output: 3

Example 3:
    Input: num = 123
    Output: 12

Approach: Bit Manipulation
- Each bit (except the highest) contributes 2 steps (subtract 1 and divide by 2)
- The highest bit contributes 1 step (don't need to divide)
- So steps = number of bits - 1 + number of 1s - 1 = bit_length - 1 + popcount - 1
- Simpler: simulate the process

Time Complexity:  O(log n) — number of bits in num
Space Complexity: O(1) — constant extra space
"""

from __future__ import annotations


def number_of_steps(num: int) -> int:
    """Return number of steps to reduce num to 0."""
    steps = 0
    
    while num > 0:
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
        steps += 1
    
    return steps


# Bit manipulation approach (more efficient insight)
def number_of_steps_bits(num: int) -> int:
    """
    Using bit manipulation:
    - Each '1' bit (except the MSB) contributes 2 steps
    - Each '0' bit contributes 1 step
    - Total = bit_length - 1 + popcount
    """
    if num == 0:
        return 0
    
    # For n in binary:
    # - Each 1 needs a subtract step
    # - Each position needs a divide step (except the last one)
    # Steps = bit_length + popcount - 1
    return num.bit_length() + bin(num).count('1') - 1


# ── Inline Tests ──────────────────────────────────────────────────────────────

def _test_number_of_steps():
    # Example 1
    assert number_of_steps(14) == 6
    assert number_of_steps_bits(14) == 6
    
    # Example 2
    assert number_of_steps(8) == 3
    assert number_of_steps_bits(8) == 3
    
    # Example 3
    assert number_of_steps(123) == 12
    assert number_of_steps_bits(123) == 12
    
    # Zero
    assert number_of_steps(0) == 0
    assert number_of_steps_bits(0) == 0
    
    # One
    assert number_of_steps(1) == 1
    assert number_of_steps_bits(1) == 1
    
    # Power of 2
    assert number_of_steps(16) == 4  # 16 -> 8 -> 4 -> 2 -> 1 -> 0? No, 16->8->4->2->1->0 is 5 steps
    assert number_of_steps_bits(16) == 5
    
    # Two
    assert number_of_steps(2) == 2  # 2 -> 1 -> 0
    assert number_of_steps_bits(2) == 2
    
    # Three
    assert number_of_steps(3) == 3  # 3 -> 2 -> 1 -> 0
    assert number_of_steps_bits(3) == 3
    
    # Large number
    assert number_of_steps(100) == 7
    assert number_of_steps_bits(100) == 7
    
    print("All Number of Steps to Reduce a Number to Zero tests passed!")


if __name__ == "__main__":
    _test_number_of_steps()