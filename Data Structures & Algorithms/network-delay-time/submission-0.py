class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u-1].append((v-1,w))

        dist = [float('inf')] * n

        dist[k-1] = 0
        minHeap = [(0,k-1)]

        while minHeap:
            time, node = heapq.heappop(minHeap)

            if time > dist[node]:
                continue

            for nei, wt in graph[node]:
                newTime = time + wt
                if newTime < dist[nei]:
                    dist[nei] = newTime
                    heapq.heappush(minHeap, (newTime, nei))

        maxTime = max(dist)
        return maxTime if maxTime != float('inf') else -1 


        