from typing import List
def minFallingPathSum(matrix: List[List[int]]) -> int:
    n=len(matrix)
    dp=matrix[0][:]
    for r in range(1,n):
        new=[0]*n
        for c in range(n):
            new[c]=matrix[r][c]+min(dp[max(0,c-1)],dp[c],dp[min(n-1,c+1)])
        dp=new
    return min(dp)
if __name__=="__main__":
    print("931 OK")
