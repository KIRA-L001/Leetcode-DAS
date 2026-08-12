"""
LeetCode #68 - Text Justification
Difficulty: Hard
"""
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0
        while i < len(words):
            line_len = len(words[i])
            j = i + 1
            while j < len(words) and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1
            line = words[i:j]
            spaces = maxWidth - sum(len(w) for w in line)
            if j == len(words) or len(line) == 1:
                result.append(" ".join(line) + " " * (spaces - (len(line) - 1)))
            else:
                gaps = len(line) - 1
                base, extra = spaces // gaps, spaces % gaps
                s = ""
                for k in range(gaps):
                    s += line[k] + " " * (base + (1 if k < extra else 0))
                s += line[-1]
                result.append(s)
            i = j
        return result
