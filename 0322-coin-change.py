"""
322. Coin Change
Given coin denominations and amount, return the fewest coins needed (or -1 if impossible).

Approach: Bottom-up DP. dp[a] = min coins for amount a; dp[a] = min(dp[a-c]+1) over coins.
Time: O(amount * len(coins))  Space: O(amount).
"""
from typing import List

def coinChange(coins: List[int], amount: int) -> int:
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] <= amount else -1

if __name__ == "__main__":
    assert coinChange([1, 2, 5], 11) == 3
    assert coinChange([2], 3) == -1
    assert coinChange([1], 0) == 0
    print("0322 OK")
