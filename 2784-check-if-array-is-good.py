"""
LeetCode 2784. Check if Array is Good (Easy)

Problem:
    An array nums is good if exactly one element appears exactly once and every
    other element appears exactly twice. Return true if nums is good.

Approach:
    Count frequencies; the array is good iff exactly one value has frequency 1
    and all remaining values have frequency 2.

Complexity:
    Time:  O(n).
    Space: O(n) for the counter.
"""


def is_good(nums):
    """Return whether nums has exactly one singleton and otherwise pairs."""
    from collections import Counter
    counts = Counter(nums)
    return sum(1 for v in counts.values() if v == 1) == 1 and all(
        v == 2 for v in counts.values() if v != 1
    )


if __name__ == "__main__":
    assert is_good([2, 1, 2, 3, 3]) is True
    assert is_good([1, 2]) is False
    print("All tests passed for 2784-check-if-array-is-good")
