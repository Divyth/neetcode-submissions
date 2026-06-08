class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def bfs(r,c):
            q = deque([(r,c)])
            visit.add((r,c))
            perimeter = 0

            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx , ny = x + dx, y+dy
                    if (nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] == 0):
                        perimeter += 1
                    elif (nx,ny) not in visit:
                        visit.add((nx,ny))
                        q.append((nx,ny))

            return perimeter
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return bfs(i,j)

        return 0