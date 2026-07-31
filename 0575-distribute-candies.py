def distributeCandies(n: int, limit: int) -> int:
    # place candies with at most limit per child
    # DP / combinatorics: number of ways to give n to 3 children with cap limit
    # Use stars-and-bars with inclusion-exclusion
    total = 0
    for a in range(limit+1):
        for b in range(limit+1):
            c = n - a - b
            if 0 <= c <= limit:
                total += 1
    return total
if __name__ == "__main__":
    assert distributeCandies(5, 2) > 0
    print("575 OK")
