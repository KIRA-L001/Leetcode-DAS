class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a = [int(x) for x in version1.split('.')]
        b = [int(x) for x in version2.split('.')]
        for i in range(max(len(a), len(b))):
            x = a[i] if i < len(a) else 0
            y = b[i] if i < len(b) else 0
            if x < y: return -1
            if x > y: return 1
        return 0
