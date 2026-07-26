"""
LeetCode 0022 - Generate Parentheses (Medium)

Generate all combinations of n pairs of well-formed parentheses.

Approach: backtracking. Add '(' while we still have opens left, and
add ')' only while it would not unbalance the string.

Time:  O(4^n / sqrt(n))  (Catalan number of results)
Space: O(n) recursion depth (excluding output)
"""


def generate_parenthesis(n: int) -> list[str]:
    out: list[str] = []

    def back(cur: str, opens: int, closes: int) -> None:
        if len(cur) == 2 * n:
            out.append(cur)
            return
        if opens < n:
            back(cur + "(", opens + 1, closes)
        if closes < opens:
            back(cur + ")", opens, closes + 1)

    back("", 0, 0)
    return out


if __name__ == "__main__":
    assert sorted(generate_parenthesis(1)) == ["()"]
    assert sorted(generate_parenthesis(2)) == ["(())", "()()"]
    assert len(generate_parenthesis(3)) == 5  # Catalan(3)
    assert "((()))" in generate_parenthesis(3)
    print("0022 OK")
