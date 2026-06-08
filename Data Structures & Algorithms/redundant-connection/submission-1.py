class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = [i for i in range(len(edges) + 1)]
        size = [1] * (len(edges)+1)

        def find(n):
            p = parent[n]
            while p != parent[p]:           
                parent[p] = parent[parent[p]] ##  path  
                p = parent[p]                 ##  compression
            return p
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return False
            if size[p1] > size[p2]:
                parent[p2] = p1
                size[p1] += size[p2]
            else:
                parent[p1] = p2
                size[p2] += size[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]