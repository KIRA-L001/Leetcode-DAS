"""
LeetCode 2678. Number of Senior Citizens (Easy)

Problem:
    You are given a 0-indexed array of strings details. Each string is a
    record "XXXXXXXXXXMMDDYYYY" where indices 11 and 12 (0-indexed) encode the
    person's age as a two-digit number. Return the number of senior citizens
    (age >= 60).

Approach:
    Slice the two age characters from each record and count those >= 60.

Complexity:
    Time:  O(n).
    Space: O(1).
"""


def count_seniors(details):
    """Return the number of records whose encoded age is 60 or more."""
    return sum(1 for d in details if int(d[11:13]) >= 60)


if __name__ == "__main__":
    assert count_seniors(
        ["7868190130M7522", "5303914400F9211", "9279482640M3955"]
    ) == 2
    assert count_seniors(["1313579440F2036", "2922610970M7567"]) == 1
    print("All tests passed for 2678-number-of-senior-citizens")
