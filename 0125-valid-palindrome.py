"""
LeetCode #125 - Valid Palindrome
Difficulty: Easy
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [c.lower() for c in s if c.isalnum()]
        return filtered == filtered[::-1]
