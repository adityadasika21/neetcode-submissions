class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l , r = 0, (ROWS*COLS) - 1

        while l <= r: 

            m = (l + r )// 2

            row, col = m // COLS, m % COLS

            value = matrix[row][col]

            if value> target: 
                r = m - 1
            elif value < target : 
                l = m + 1
            else : 
                return True
        
        return False