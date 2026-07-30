"""
724. Find Pivot Index
Find leftmost index where left sum == right sum.
Approach: total sum, iterate subtracting from right side.
Time: O(n)  Space: O(1)
"""
def pivotIndex(nums):
    total = sum(nums)
    left = 0
    for i, x in enumerate(nums):
        if left == total - left - x: return i
        left += x
    return -1
if __name__ == "__main__":
    assert pivotIndex([1,7,3,6,5,6]) == 3
    assert pivotIndex([1,2,3]) == -1
    print("0724 OK")
