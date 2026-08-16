"""
LeetCode 1108. Defanging an IP Address (Easy)

Problem:
    Given a valid IPv4 address address, return the defanged version where
    every '.' is replaced by "[.]".

Approach:
    Use str.replace to swap every dot for the bracketed form. A single
    linear scan over the string is sufficient.

Complexity:
    Time:  O(n) - one pass over the address.
    Space: O(n) - result string.
"""


def defang_i_paddr(address):
    """Return the defanged version of a valid IPv4 address."""
    return address.replace(".", "[.]")


if __name__ == "__main__":
    assert defang_i_paddr("1.1.1.1") == "1[.]1[.]1[.]1"
    assert defang_i_paddr("255.100.50.0") == "255[.]100[.]50[.]0"
    print("All tests passed for 1108-defanging-an-ip-address")
