"""
LeetCode 2682. Find the Loser of the Circular Game (Easy)

Problem:
    n friends numbered 1..n sit in a circle. Starting at friend 1, you count k
    friends clockwise (including the starting friend) and eliminate that friend.
    Repeat until one friend remains, who is the loser. Return that friend's
    number.

Approach:
    Simulate elimination with a list, advancing the index by k-1 each round and
    removing the friend at that index (wrapping with modulo).

Complexity:
    Time:  O(n^2).
    Space: O(n).
"""


def circular_game_loser(n, k):
    """Return the last remaining friend after the elimination game."""
    friends = list(range(1, n + 1))
    idx = 0
    while len(friends) > 1:
        idx = (idx + k - 1) % len(friends)
        friends.pop(idx)
    return friends[0]


if __name__ == "__main__":
    assert circular_game_loser(5, 2) == 3
    assert circular_game_loser(6, 3) == 1
    print("All tests passed for 2682-find-the-loser-of-the-circular-game")
