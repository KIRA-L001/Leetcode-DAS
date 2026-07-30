"""
692. Top K Frequent Words
Return the k most frequent words sorted by frequency desc, then lexicographically.
Approach: Count with Counter, sort by (-freq, word).
Time: O(n log n)  Space: O(n)
"""
from collections import Counter
def topKFrequent(words, k):
    c = Counter(words)
    return sorted(c, key=lambda w: (-c[w], w))[:k]
if __name__ == "__main__":
    assert topKFrequent(["i","love","leetcode","i","love","coding"], 2) == ["i","love"]
    print("0692 OK")
