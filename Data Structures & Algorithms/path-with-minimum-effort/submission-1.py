class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = 0

        minHeap = [(0,0,0)]

        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        
        while minHeap:
            effort, r, c = heapq.heappop(minHeap)

            if r == rows - 1 and c == cols - 1:
                return effort

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    newEffort = max(effort, abs(heights[r][c] - heights[nr][nc]))

                    if newEffort < dist[nr][nc]:
                        dist[nr][nc] = newEffort
                        heapq.heappush(minHeap, (newEffort, nr, nc))
        return 0
