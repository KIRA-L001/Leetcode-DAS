
"""
LeetCode #30 - Substring with Concatenation of All Words
Difficulty: Hard
"""
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = {}
        for w in words:
            word_count[w] = word_count.get(w, 0) + 1
        result = []
        for i in range(len(s) - total_len + 1):
            seen = {}
            j = 0
            while j < num_words:
                word = s[i + j*word_len : i + (j+1)*word_len]
                if word not in word_count:
                    break
                seen[word] = seen.get(word, 0) + 1
                if seen[word] > word_count.get(word, 0):
                    break
                j += 1
            if j == num_words:
                result.append(i)
        return result
