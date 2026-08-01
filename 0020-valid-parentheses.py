"""
LeetCode #20 - Valid Parentheses
Difficulty: Easy
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in pairs.values():
                stack.append(c)
            elif not stack or stack.pop() != pairs[c]:
                return False
        return not stack
