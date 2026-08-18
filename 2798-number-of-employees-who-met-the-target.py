"""
LeetCode 2798. Number of Employees Who Met the Target (Easy)

Problem:
    Given an array hours where hours[i] is the hours the ith employee worked,
    and an integer target, return the number of employees who worked at least
    target hours.

Approach:
    Count values >= target.

Complexity:
    Time:  O(n).
    Space: O(1).
"""


def number_of_employees_who_met_target(hours, target):
    """Return the count of employees with hours >= target."""
    return sum(1 for h in hours if h >= target)


if __name__ == "__main__":
    assert number_of_employees_who_met_target([0, 1, 2, 3, 4], 2) == 3
    assert number_of_employees_who_met_target([5, 1, 4, 2, 2], 6) == 0
    print("All tests passed for 2798-number-of-employees-who-met-the-target")
