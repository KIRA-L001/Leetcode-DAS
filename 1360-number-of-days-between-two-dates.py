"""
# 1360. Number of Days Between Two Dates (Easy)
# Write a program to count the number of days between two given dates in YYYY-MM-DD format.

# NeetCode 150 / Blind 75: Date / Math

Example 1:
    Input: date1 = "2020-01-15", date2 = "2020-08-20"
    Output: 218

Example 2:
    Input: date1 = "2020-07-15", date2 = "2021-07-15"
    Output: 366

Example 3:
    Input: date1 = "2019-06-29", date2 = "2020-01-01"
    Output: 193

Approach: Use datetime module
- Parse dates using datetime.strptime
- Calculate absolute difference
- Return number of days

Time Complexity:  O(1)
Space Complexity: O(1)
"""

from __future__ import annotations
from datetime import datetime


def days_between(date1: str, date2: str) -> int:
    """Return absolute number of days between two dates in YYYY-MM-DD format."""
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    return abs((d2 - d1).days)


# ── Inline Tests ──────────────────────────────────────────────────────────────

def _test_days_between():
    # Example 1
    assert days_between("2020-01-15", "2020-08-20") == 218
    
    # Example 2
    assert days_between("2020-07-15", "2021-07-15") == 366  # 2020 is leap year
    
    # Example 3
    assert days_between("2019-06-29", "2020-01-01") == 193
    
    # Same date
    assert days_between("2020-01-01", "2020-01-01") == 0
    
    # Reverse order
    assert days_between("2020-08-20", "2020-01-15") == 218
    
    # Leap year
    assert days_between("2020-02-28", "2020-03-01") == 2  # 2020 is leap year
    assert days_between("2021-02-28", "2021-03-01") == 1  # 2021 is not leap year
    
    # One year apart
    assert days_between("2020-01-01", "2021-01-01") == 366
    
    # Large span
    assert days_between("2000-01-01", "2020-01-01") == 7305
    
    print("All Number of Days Between Two Dates tests passed!")


if __name__ == "__main__":
    _test_days_between()