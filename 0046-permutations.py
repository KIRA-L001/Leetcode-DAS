"""
LeetCode 0046 - Permutations (Medium)

Return all permutations of a list of distinct integers.

Approach: backtracking with a used-marker; build each permutation by
choosing an unused element at every depth.

Time:  O(n * n!)
Space: O(n) recursion/state (excluding output)
"""


def permute(nums: list[int]) -> list[list[int]]:
    out: list[list[int]] = []
    used = [False] * len(nums)
    path: list[int] = []

    def back() -> None:
        if len(path) == len(nums):
            out.append(path[:])
            return
        for i, v in enumerate(nums):
            if used[i]:
                continue
            used[i] = True
            path.append(v)
            back()
            path.pop()
            used[i] = False

    back()
    return out


if __name__ == "__main__":
    res = permute([1, 2, 3])
    assert len(res) == 6
    assert [1, 2, 3] in res and [3, 2, 1] in res
    assert permute([1]) == [[1]]
    print("0046 OK")
