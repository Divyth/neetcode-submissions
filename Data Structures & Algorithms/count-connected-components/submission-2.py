class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        
        if px == py:
            return False # already connected

        if self.rank[px] > self.rank[py]: # rank is not increased since attaching a smaller deosnt increase the eank
            self.parent[py] = px
        elif self.rank[py] > self.rank[px]:
            self.parent[px] = py

        else: # rank only increase when both have same ranks
            self.parent[px] = py
            self.rank[py] += 1
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = n
        dsu = DSU(n)

        for u, v in edges:
            if dsu.union(u, v):
                components -= 1
        return components
        
        