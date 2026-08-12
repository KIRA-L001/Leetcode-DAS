"""
LeetCode #65 - Valid Number
Difficulty: Hard
"""
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False
        has_num = has_dot = has_e = False
        for i, c in enumerate(s):
            if c.isdigit():
                has_num = True
            elif c in '+.-':
                if i != 0 and s[i-1] != 'e':
                    return False
            elif c == 'e':
                if has_e or not has_num:
                    return False
                has_e = True
                has_num = False
            elif c == '.':
                if has_dot or has_e:
                    return False
                has_dot = True
            else:
                return False
        return has_num
