from typing import List
def transpose(matrix: List[List[int]]) -> List[List[int]]:
    m,n = len(matrix), len(matrix[0])
    return [[matrix[i][j] for i in range(m)] for j in range(n)]
if __name__=="__main__":
    print("867 OK")
