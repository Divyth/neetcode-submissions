class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        def bfs(starts):
            visited = set(starts)

            q = deque(starts)

            while q:
                r, c = q.popleft()

                for dr, dc in [(-1,0),(0,1),(0,-1),(1,0)]:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr,nc) not in visited and heights[nr][nc] >= heights[r][c]:
                        visited.add((nr,nc))
                        q.append((nr,nc))
                        
            return visited
        
        pacificStart = []
        atlanticStart = []

        for c in range(COLS):
            pacificStart.append((0, c))
            atlanticStart.append((ROWS-1, c))

        for r in range(ROWS):
            pacificStart.append((r,0))
            atlanticStart.append((r,COLS-1))

        pacific = bfs(pacificStart)
        atlantic = bfs(atlanticStart)
        
        res = []
        for cell in pacific:
            if cell in atlantic:
                res.append(cell)
        return res
        
        

       


        


         
        