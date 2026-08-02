"""
122. Best Time to Buy and Sell Stock II (Easy)

Problem:
    You are given an integer array prices where prices[i] is the price of a
    given stock on the i-th day. On each day, you may decide to buy and/or
    sell the stock. You can hold at most one share of the stock at any time.
    However, you may buy it then immediately sell it on the same day.

    Find and return the maximum profit you can achieve.

Approach:
    Greedy — accumulate every positive price difference between consecutive
    days. Since there is no transaction limit, we can capture every upward
    slope in the price curve.

Time Complexity:  O(n) — single pass through the array
Space Complexity: O(1) — only two variables

Example:
    >>> prices = [7, 1, 5, 3, 6, 4]
    >>> max_profit(prices)
    7
    >>> prices = [1, 2, 3, 4, 5]
    >>> max_profit(prices)
    4
    >>> prices = [7, 6, 4, 3, 1]
    >>> max_profit(prices)
    0
"""


def max_profit(prices: list[int]) -> int:
    """Return the maximum profit from unlimited stock transactions."""
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit


def max_profit_one_liner(prices: list[int]) -> int:
    """One-liner using sum and zip."""
    return sum(b - a for a, b in zip(prices, prices[1:]) if b > a)


if __name__ == "__main__":
    # Inline tests
    assert max_profit([7, 1, 5, 3, 6, 4]) == 7, "Test 1 failed"
    assert max_profit([1, 2, 3, 4, 5]) == 4, "Test 2 failed"
    assert max_profit([7, 6, 4, 3, 1]) == 0, "Test 3 failed"
    assert max_profit([1, 2]) == 1, "Test 4 failed"
    assert max_profit([2, 1]) == 0, "Test 5 failed"
    assert max_profit([]) == 0, "Test 6 failed"
    assert max_profit([5]) == 0, "Test 7 failed"

    # One-liner parity checks
    for tc in [[7, 1, 5, 3, 6, 4], [1, 2, 3, 4, 5], [7, 6, 4, 3, 1], [1, 2], [2, 1], [], [5]]:
        assert max_profit(tc) == max_profit_one_liner(tc), f"Parity failed for {tc}"

    print("All tests passed.")
