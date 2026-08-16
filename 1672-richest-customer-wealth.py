"""
LeetCode 1672. Richest Customer Wealth (Easy)

Problem:
    Given an m x n integer matrix accounts where accounts[i][j] is the
    amount of money the i-th customer has in the j-th bank, return the
    wealth of the richest customer (sum of their bank balances).

Approach:
    Sum each row and take the maximum over all rows.

Complexity:
    Time:  O(m * n) - visit every cell once.
    Space: O(1) - no extra storage beyond the running maximum.
"""


def maximum_wealth(accounts):
    """Return the largest row-sum across the accounts matrix."""
    return max(sum(row) for row in accounts)


if __name__ == "__main__":
    assert maximum_wealth([[1, 2, 3], [3, 2, 1]]) == 6
    assert maximum_wealth([[1, 5], [7, 3], [3, 5]]) == 10
    assert maximum_wealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]) == 17
    print("All tests passed for 1672-richest-customer-wealth")
