import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return t == t[::-1]

# refreshed 20260823-123438
