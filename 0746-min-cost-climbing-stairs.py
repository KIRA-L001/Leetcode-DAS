"""
746. Min Cost Climbing Stairs
Pay cost[i] to step on i; start at step 0 or 1. Min cost to reach top (n).
Approach: DP — min cost to reach i = cost[i] + min(cost[i-1], cost[i-2]).
Time: O(n)  Space: O(1)
"""
def minCostClimbingStairs(cost):
    n = len(cost)
    prev2, prev1 = cost[0], cost[1]
    for i in range(2, n):
        curr = cost[i] + min(prev1, prev2)
        prev2, prev1 = prev1, curr
    return min(prev1, prev2)
if __name__ == "__main__":
    assert minCostClimbingStairs([10,15,20]) == 15
    assert minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]) == 6
    print("0746 OK")
