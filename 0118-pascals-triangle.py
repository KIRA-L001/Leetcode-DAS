"""
118. Pascal's Triangle (Easy)

Problem:
    Given an integer numRows, return a 2D list representing Pascal's triangle
    with numRows rows. In Pascal's triangle, each number is the sum of the
    two numbers directly above it.

Approach:
    Build each row iteratively. The first row is [1]. Each subsequent row
    starts and ends with 1, and middle elements are the sum of the two
    elements above them from the previous row.

Complexity:
    Time:  O(n^2) where n is numRows - sum of 1+2+3+...+n = n*(n+1)/2.
    Space: O(n^2) - for storing all rows.
"""


def generate(num_rows):
    """Generate Pascal's triangle with the given number of rows."""
    triangle = []
    
    for row_num in range(num_rows):
        # First and last elements are always 1
        row = [1] * (row_num + 1)
        
        # Fill middle elements
        for j in range(1, row_num):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
        
        triangle.append(row)
    
    return triangle


if __name__ == "__main__":
    # Test 1: 5 rows
    expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert generate(5) == expected
    
    # Test 2: 1 row
    assert generate(1) == [[1]]
    
    # Test 3: 6 rows - verify middle elements
    result6 = generate(6)
    assert result6[5] == [1, 5, 10, 10, 5, 1]
    
    print("All tests passed for 0118-pascals-triangle")