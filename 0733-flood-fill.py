"""
733. Flood Fill
Replace connected pixels of same color starting from (sr, sc).
Approach: BFS/DFS from start pixel, change colors matching original.
Time: O(m*n)  Space: O(m*n)
"""
def floodFill(image, sr, sc, color):
    if not image: return image
    orig = image[sr][sc]
    if orig == color: return image
    rows, cols = len(image), len(image[0])
    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or image[r][c] != orig: return
        image[r][c] = color
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            dfs(r+dr, c+dc)
    dfs(sr, sc)
    return image
if __name__ == "__main__":
    assert floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2) == [[2,2,2],[2,2,0],[2,0,1]]
    print("0733 OK")
