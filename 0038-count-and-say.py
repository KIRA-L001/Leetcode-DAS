"""
38. Count and Say (Easy)

Problem:
    Given a positive integer n, generate the nth sequence of the count-and-say
    sequence. The count-and-say sequence is a sequence of digit strings.

Approach:
    Build the sequence iteratively. For each level, read the previous sequence
    and generate the next by counting consecutive identical digits and appending
    count followed by digit to the result.

Complexity:
    Time:  O(n * m) where m is the length of the nth sequence.
    Space: O(m) for storing the current sequence.
"""


def count_and_say(n):
    """Generate the nth count-and-say sequence."""
    if n == 1:
        return "1"
    
    prev = "1"
    for _ in range(2, n + 1):
        curr = []
        i = 0
        while i < len(prev):
            count = 1
            while i + 1 < len(prev) and prev[i] == prev[i + 1]:
                count += 1
                i += 1
            curr.append(str(count) + prev[i])
            i += 1
        prev = "".join(curr)
    return prev


if __name__ == "__main__":
    assert count_and_say(1) == "1"
    assert count_and_say(4) == "1211"
    assert count_and_say(5) == "111221"
    
    print("All tests passed for 0038-count-and-say")