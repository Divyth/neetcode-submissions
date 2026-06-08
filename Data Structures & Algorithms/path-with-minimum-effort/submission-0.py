class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        
        dist = [[float('inf')] * cols for _ in range(rows) ]
        dist[0][0] = 0

        minHeap = [[0,0,0]]

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)

            if (r,c) == (rows-1,cols-1):
                return diff

            if diff > dist[r][c]:
                continue
            
            for dr, dc in directions:
                nr, nc = r + dr, c +dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    edgediff = abs(heights[nr][nc] - heights[r][c])
                    newDiff = max(diff, edgediff)

                    if newDiff < dist[nr][nc]:
                        dist[nr][nc] = newDiff
                        heapq.heappush(minHeap, (newDiff, nr,nc))

        return 0


        