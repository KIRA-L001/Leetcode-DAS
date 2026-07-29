"""
383. Ransom Note
Given strings ransomNote and magazine, return True if ransomNote can be constructed
from magazine letters (each letter used once).

Approach: Counter subtraction; if any count goes negative, return False.
Time: O(m)  Space: O(26)
"""
from typing import List
from collections import Counter

def canConstruct(ransomNote: str, magazine: str) -> bool:
    c = Counter(magazine)
    for ch in ransomNote:
        c[ch] -= 1
        if c[ch] < 0:
            return False
    return True

if __name__ == "__main__":
    assert canConstruct("a", "b") is False
    assert canConstruct("aa", "ab") is False
    assert canConstruct("aa", "aab") is True
    print("0383 OK")