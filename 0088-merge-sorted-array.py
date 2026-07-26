"""
LeetCode 0088 - Merge Sorted Array (Easy)

Merge nums2 into nums1 in place (nums1 has m valid elements + n slots).

Approach: three pointers from the back; place the larger tail element
into the last free slot so nothing valid is overwritten.

Time:  O(m + n)
Space: O(1)
"""


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1


if __name__ == "__main__":
    a = [1, 2, 3, 0, 0, 0]
    merge(a, 3, [2, 5, 6], 3)
    assert a == [1, 2, 2, 3, 5, 6]

    b = [1]
    merge(b, 1, [], 0)
    assert b == [1]

    c = [0]
    merge(c, 0, [1], 1)
    assert c == [1]
    print("0088 OK")
