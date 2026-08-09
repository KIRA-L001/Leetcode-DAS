"""
LeetCode #58 - Length of Last Word
Difficulty: Easy
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split()[-1])
