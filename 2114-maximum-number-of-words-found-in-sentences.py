"""
LeetCode 2114. Maximum Number of Words Found in Sentences (Easy)

Problem:
    Given a list of sentences (each a string of words separated by single
    spaces), return the maximum number of words in a single sentence.

Approach:
    Split each sentence on whitespace and take the maximum resulting length.

Complexity:
    Time:  O(total characters across all sentences).
    Space: O(1) extra beyond the temporary split lists.
"""


def most_words_found(sentences):
    """Return the largest word count among the given sentences."""
    return max(len(s.split()) for s in sentences)


if __name__ == "__main__":
    assert most_words_found(["alice and bob", "the quick brown fox"]) == 4
    assert most_words_found(["a", "b c", "d e f"]) == 3
    print("All tests passed for 2114-maximum-number-of-words-found-in-sentences")
