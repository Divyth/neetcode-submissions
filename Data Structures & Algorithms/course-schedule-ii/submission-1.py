class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses

        adj = [[] for _ in range(numCourses)]
        res = []
      
        for u, v in prerequisites:
            adj[u].append(v)
            indegree[v] += 1

        q = deque()

        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            res.append(node)
            

            for nei in adj[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)
        return res[::-1] if len(res) == numCourses else []
