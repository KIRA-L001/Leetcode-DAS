"""
121. Best Time to Buy and Sell Stock (Easy)

Problem:
    Given prices[i] = stock price on day i, choose one day to buy and a
    later day to sell to maximize profit. Return the max profit (0 if none).

Approach:
    One pass, tracking the minimum price seen so far and the best profit
    achievable by selling today.

Complexity:
    Time:  O(n)
    Space: O(1)
"""


def max_profit(prices):
    min_price = float("inf")
    best = 0
    for p in prices:
        min_price = min(min_price, p)      # cheapest buy so far
        best = max(best, p - min_price)    # profit selling today
    return best


if __name__ == "__main__":
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5  # buy 1, sell 6
    assert max_profit([7, 6, 4, 3, 1]) == 0     # always falling
    assert max_profit([2, 4, 1]) == 2
    assert max_profit([]) == 0
    print("All tests passed for 0121-best-time-to-buy-and-sell-stock")
