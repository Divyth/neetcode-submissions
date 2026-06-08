class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        rowBegin = 0
        rowEnd = len(matrix) -1 
        colBegin = 0
        colEnd = len(matrix[0]) - 1

        res = []
        while rowBegin <= rowEnd and colBegin <= colEnd:
            for col in range(colBegin, colEnd + 1):
                res.append(matrix[rowBegin][col])
            rowBegin += 1

            for row in range(rowBegin, rowEnd +1):
                res.append(matrix[row][colEnd])
            colEnd -= 1
            
            if rowBegin <= rowEnd:
                for col in range(colEnd, colBegin -1 , -1):
                    res.append(matrix[rowEnd][col])
                rowEnd -= 1

            if colBegin <= colEnd:
                for row in range(rowEnd, rowBegin -1 , -1):
                    res.append(matrix[row][colBegin])

                colBegin += 1

        return res

        