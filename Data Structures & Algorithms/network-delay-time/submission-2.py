class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]
        
        for u, v, w in times:
            adj[u].append((v,w))
        
        dist = [float('inf')] * (n+1)
        dist[k] = 0
        minHeap = [(0,k)]

        while minHeap:
            time, node = heapq.heappop(minHeap)

            if time > dist[node]:
                continue
            
            for nei, wt in adj[node]:
                if dist[nei] > time + wt:
                    dist[nei] = time + wt
                    heapq.heappush(minHeap, (dist[nei], nei))
        
        maxTime = max(dist[1:])
        return maxTime if maxTime != float('inf') else -1

    