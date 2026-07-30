"""
566. Reshape the Matrix
Given matrix and target (r, c), reshape if possible.
Approach: row-major flatten then repopulate.
Time: O(m*n)  Space: O(r*c)
"""
def matrixReshape(mat, r, c):
    m, n = len(mat), len(mat[0])
    if m*n != r*c: return mat
    flat = [x for row in mat for x in row]
    return [flat[i:i+c] for i in range(0, r*c, c)]
if __name__ == "__main__":
    assert matrixReshape([[1,2],[3,4]], 1, 4) == [[1,2,3,4]]
    print("0566 OK")
