class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        Rows = len(matrix)
        Cols = len(matrix[0])

        dp = {} #memo/cache key -> value = (r,c) -> res

        def dfs(r, c):
            if (r,c) in dp:
                return dp[(r,c)]
            
            res = 1

            for dr, dc in [(1,0),(0,-1),(-1,0),(0,1)]:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < Rows and 0 <= nc < Cols and matrix[nr][nc] > matrix[r][c]):
                    res = max(res, 1 + dfs(nr, nc))

            
            dp[(r,c)] = res

            return res

        ans = 0
        
        for r in range(Rows):
            for c in range(Cols):
                ans = max(ans, dfs(r,c))

        return ans


        