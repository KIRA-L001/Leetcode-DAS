"""
LeetCode 2566. Maximum Difference by Remapping a Digit (Easy)

Problem:
    You are given an integer num. You can remap exactly one digit x to another
    digit y (x != y) in the decimal representation of num, replacing every
    occurrence of x with y. Return the maximum possible difference between the
    largest and smallest values you can obtain.

Approach:
    Try every ordered pair (x, y) of digits with x != y. For each, build the
    remapped integer and track the minimum and maximum obtainable values, then
    return max - min.

Complexity:
    Time:  O(d) where d <= 10 digits (constant bound).
    Space: O(1).
"""


def min_max_difference(num):
    """Return max - min value achievable by remapping one digit."""
    s = str(num)
    lo = num
    hi = num
    for x in "0123456789":
        if x not in s:
            continue
        for y in "0123456789":
            if x == y:
                continue
            val = int(s.replace(x, y))
            lo = min(lo, val)
            hi = max(hi, val)
    return hi - lo


if __name__ == "__main__":
    assert min_max_difference(11891) == 99009
    assert min_max_difference(90) == 99
    assert min_max_difference(555) == 999
    print("All tests passed for 2566-maximum-difference-by-remapping-a-digit")
