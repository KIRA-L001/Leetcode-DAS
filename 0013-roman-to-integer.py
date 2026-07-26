"""
LeetCode 0013 - Roman to Integer (Easy)

Convert a Roman numeral string to an integer.

Approach: scan left to right; if a symbol is smaller than the one after
it, subtract it (subtractive notation), otherwise add it.

Time:  O(n)
Space: O(1)
"""

VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_to_int(s: str) -> int:
    total = 0
    for i, ch in enumerate(s):
        v = VALUES[ch]
        # subtractive pair like IV, IX, XL ...
        if i + 1 < len(s) and v < VALUES[s[i + 1]]:
            total -= v
        else:
            total += v
    return total


if __name__ == "__main__":
    assert roman_to_int("III") == 3
    assert roman_to_int("LVIII") == 58
    assert roman_to_int("MCMXCIV") == 1994
    assert roman_to_int("IX") == 9
    print("0013 OK")
