class Solution:
    def reverseVowels(self, s: str) -> str:
        v = "aeiouAEIOU"; s = list(s); i, j = 0, len(s)-1
        while i < j:
            if s[i] in v and s[j] in v: s[i], s[j] = s[j], s[i]; i += 1; j -= 1
            elif s[i] in v: j -= 1
            elif s[j] in v: i += 1
            else: i += 1; j -= 1
        return "".join(s)
