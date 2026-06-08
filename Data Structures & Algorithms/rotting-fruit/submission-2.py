class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 

        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        time = 0
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
                
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        while fresh >0 and q:
            time += 1
            for _ in range(len(q)): 
                r, c = q.popleft()

                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            q.append((nr,nc))
                            fresh -= 1
            
        return time if fresh == 0 else -1
