import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return t == t[::-1]

# refreshed 20261022-205550
