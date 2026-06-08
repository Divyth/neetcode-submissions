class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        for i in range(numRows -1):
            temp = [0] + res[-1] + [0]  # paading zeros in the front and end that makes easy fro next rows elements and res[-1] is the last row that was generated
            nextRow = []

            for j in range(len(res[-1]) + 1):
                nextRow.append(temp[j] + temp[j+1])

            res.append(nextRow)

        return res
        