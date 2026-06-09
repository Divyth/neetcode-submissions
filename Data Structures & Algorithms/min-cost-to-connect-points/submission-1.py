class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        minHeap = [(0, 0)]
        totalCost = 0
        edgeUsed = 0

        while edgeUsed < n:
            cost, node = heapq.heappop(minHeap)

            if visited[node]:
                continue

            visited[node] = True
            totalCost += cost
            edgeUsed += 1

            x1, y1 = points[node]

            for v in range(n):
                if not visited[v]:
                    x2, y2 = points[v]
                    dist = abs(x1-x2) + abs(y1-y2)
                    heapq.heappush(minHeap, (dist, v))
        return totalCost


        