"""
LeetCode 2640. Find the Score of All Prefixes of an Array (Easy)

Problem:
    Given a 0-indexed integer array nums, define the score of the prefix of
    length k as the alternating sum: nums[0] - nums[1] + nums[2] - ... +/- nums[k-1].
    Return an array answer where answer[i] is the score of prefix length i+1.

Approach:
    Maintain the running alternating sum incrementally; on even index add, on
    odd index subtract.

Complexity:
    Time:  O(n).
    Space: O(n) for the answer.
"""


def find_prefix_score(nums):
    """Return the alternating-sum score of every prefix."""
    answer = []
    running = 0
    for i, x in enumerate(nums):
        if i % 2 == 0:
            running += x
        else:
            running -= x
        answer.append(running)
    return answer


if __name__ == "__main__":
    assert find_prefix_score([2, 3, 7, 5, 10]) == [2, -1, 6, 1, 11]
    assert find_prefix_score([1, 1, 1, 1]) == [1, 0, 1, 0]
    print("All tests passed for 2640-find-the-score-of-all-prefixes-of-an-array")
