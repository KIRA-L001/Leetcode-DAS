"""
LeetCode 2582. Pass the Pillow (Easy)

Problem:
    n people sit in a line indexed 1..n. The pillow starts at person 1 and is
    passed to the next person each second, reversing direction at the ends.
    Return the index of the person holding the pillow after time seconds.

Approach:
    The pillow traverses a full back-and-forth cycle of length 2*(n-1). Reduce
    time modulo the cycle, then map the remainder to a position.

Complexity:
    Time:  O(1).
    Space: O(1).
"""


def pass_the_pillow(n, time):
    """Return who holds the pillow after `time` seconds."""
    cycle = 2 * (n - 1)
    t = time % cycle
    if t <= n - 1:
        return t + 1
    return n - (t - (n - 1))


if __name__ == "__main__":
    assert pass_the_pillow(4, 5) == 2
    assert pass_the_pillow(3, 2) == 3
    assert pass_the_pillow(5, 0) == 1
    print("All tests passed for 2582-pass-the-pillow")
