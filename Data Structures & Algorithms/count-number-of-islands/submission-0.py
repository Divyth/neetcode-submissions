class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Define possible movement directions (up, down, left, right)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # Get the number of rows and columns in the grid
        ROWS, COLS = len(grid), len(grid[0])
        # Initialize the count of islands to 0
        islands = 0

        # Define a helper function to perform depth-first search (DFS)
        def dfs(r, c):
            # Check if the current cell is out of bounds or is water ("0")
            if (r < 0 or c < 0 or r >= ROWS or 
                c >= COLS or grid[r][c] == "0"):
                return

            # Mark the current cell as visited by changing it to "0"
            grid[r][c] = "0"
            # Explore all 4 possible directions
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Iterate through each cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                # If the current cell is land ("1"), it's a new island
                if grid[r][c] == "1":
                    # Perform DFS to mark all connected land cells
                    dfs(r, c)
                    # Increment the island count
                    islands += 1

        # Return the total number of islands found
        return islands
