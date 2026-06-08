class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        rowTrack = [0 for _ in range(ROWS)]
        colTrack = [0 for _ in range(COLS)]

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    rowTrack[i] = -1
                    colTrack[j] = -1

        for i in range(ROWS):
            for j in range(COLS):
                if rowTrack[i] == -1 or colTrack[j] == -1:
                    matrix[i][j] = 0

        
        
        