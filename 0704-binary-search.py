"""
704. Binary Search
Return index of target in sorted array.
Approach: Classic binary search.
Time: O(log n)  Space: O(1)
"""
def search(nums, target):
    lo, hi = 0, len(nums)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if nums[mid] == target: return mid
        if nums[mid] < target: lo = mid+1
        else: hi = mid-1
    return -1
if __name__ == "__main__":
    assert search([-1,0,3,5,9,12], 9) == 4
    assert search([-1,0,3,5,9,12], 2) == -1
    print("0704 OK")
