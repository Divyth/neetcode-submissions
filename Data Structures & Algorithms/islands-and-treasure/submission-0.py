class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Get the dimensions of the grid
        ROWS, COLS = len(grid), len(grid[0])
        
        # Set to keep track of visited cells
        visit = set()
        
        # Queue for BFS traversal
        q = deque()

        # Helper function to add valid cells to the queue
        def addCell(r, c):
            # Check if the cell is out of bounds, already visited, or has a value of -1
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                (r, c) in visit or grid[r][c] == -1):
                return  # Ignore invalid cells
            visit.add((r, c))  # Mark the cell as visited
            q.append([r, c])  # Add the cell to the queue for BFS

        # Initialize the BFS queue with all cells having value 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:  # Starting points (e.g., water or specific cells)
                    q.append([r, c])  # Add cell to the queue
                    visit.add((r, c))  # Mark it as visited

        dist = 0  # Variable to keep track of the distance from the nearest 0
        while q:  # BFS loop to process all cells in the queue
            for i in range(len(q)):  # Process all cells at the current distance level
                r, c = q.popleft()  # Remove the cell from the front of the queue
                grid[r][c] = dist  # Update the cell with the current distance
                # Explore the neighboring cells (up, down, left, right)
                addCell(r + 1, c)  # Add the cell below
                addCell(r - 1, c)  # Add the cell above
                addCell(r, c + 1)  # Add the cell to the right
                addCell(r, c - 1)  # Add the cell to the left
            dist += 1  # Increment the distance for the next layer of BFS
