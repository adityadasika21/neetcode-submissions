class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows, cols = len(matrix), len(matrix[0])
        # 3,3
        idx = []

        for r in range(rows): 
            for c in range(cols): 
                if matrix[r][c] == 0:
                    idx.append((r,c))

        for R,C in idx: 
            for r in range(rows): 
                matrix[r][C] = 0

            for c in range(cols): 
                matrix[R][c] = 0

        