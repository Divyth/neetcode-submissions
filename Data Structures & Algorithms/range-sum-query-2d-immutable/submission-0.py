class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return 
        rows = len(matrix)
        cols = len(matrix[0])

        self.prefix = [[0]* cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                top = self.prefix[i-1][j] if i > 0 else 0 
                left = self.prefix[i][j-1] if j > 0 else 0
                topleft = self.prefix[i-1][j-1] if i>0 and j>0 else 0

                self.prefix[i][j] = matrix[i][j] + top + left - topleft

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefix[row2][col2]
        left = self.prefix[row2][col1-1] if col1>0 else 0
        top = self.prefix[row1-1][col2] if row1 >0 else 0
        topleft = self.prefix[row1-1][col1-1] if row1 > 0 and col1 >0 else 0

        return total - left -top +topleft# topleft is overlapping part
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)