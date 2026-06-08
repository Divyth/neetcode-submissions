class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        dp = [[0] * (cols + 1) for _ in range(rows)]

        dp[0][0] = grid[0][0]

        for r in range(rows):
            dp[r][0] = grid[r][0] + dp[r-1][0]

        for c in range(cols):
            dp[0][c] = grid[0][c] + dp[0][c-1]

        
        for r in range(1, rows):
            for c in range(1, cols):
                dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1])

        return dp[rows-1][cols-1]
        