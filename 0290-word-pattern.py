class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words): return False
        m1, m2 = {}, {}
        for p, w in zip(pattern, words):
            if m1.get(p, w) != w or m2.get(w, p) != p: return False
            m1[p] = w; m2[w] = p
        return True
