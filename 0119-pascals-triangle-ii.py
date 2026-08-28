from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            row = [1] + [row[i] + row[i+1] for i in range(len(row))] + [1]
        return row

# refreshed 20260828-142333
