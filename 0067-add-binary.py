"""
67. Add Binary (Easy)

Problem:
    Given two binary strings a and b, return their sum as a binary string.

Approach:
    Simulate binary addition from right to left with carry. Traverse both
    strings from the end, sum bits and carry, determine new bit and carry.

Complexity:
    Time:  O(max(n, m)) where n and m are lengths of a and b.
    Space: O(max(n, m)) for the result string.
"""


def add_binary(a, b):
    """Add two binary strings and return the result as a binary string."""
    result = []
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    
    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1
        result.append(str(total % 2))
        carry = total // 2
    
    return ''.join(reversed(result))


if __name__ == "__main__":
    assert add_binary("11", "1") == "100"
    assert add_binary("1010", "1011") == "10101"
    assert add_binary("0", "0") == "0"
    assert add_binary("1", "1") == "10"
    
    print("All tests passed for 0067-add-binary")