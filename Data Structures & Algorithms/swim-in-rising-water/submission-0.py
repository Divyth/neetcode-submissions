class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        visited = set()
        minHeap = [(grid[0][0], 0, 0)] # maxSoFar, r, c
        maxSoFar = grid[0][0]

        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        while minHeap:
            maxSoFar , r, c = heapq.heappop(minHeap)

            if r == (rows - 1) and c == (cols - 1):
                return maxSoFar
            
            if (r,c) in visited:
                continue
            visited.add((r,c))

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    newMax = max(grid[nr][nc], maxSoFar)
                    heapq.heappush(minHeap, (newMax, nr, nc))
        

            


        