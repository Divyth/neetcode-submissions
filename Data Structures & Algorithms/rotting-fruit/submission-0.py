class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Initialize a queue to perform Breadth-First Search (BFS)
        q = collections.deque()
        
        # Initialize variables to track the number of fresh oranges and the time taken
        fresh = 0  # Count of fresh oranges
        time = 0   # Time required to rot all oranges

        # Traverse the grid to count fresh oranges and enqueue all initially rotten oranges
        for r in range(len(grid)):  # Loop through all rows
            for c in range(len(grid[0])):  # Loop through all columns
                if grid[r][c] == 1:  # If the orange is fresh
                    fresh += 1
                if grid[r][c] == 2:  # If the orange is rotten
                    q.append((r, c))  # Add its position to the queue

        # Define the four possible directions (right, left, down, up)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # Perform BFS while there are fresh oranges and the queue is not empty
        while fresh > 0 and q:
            length = len(q)  # Number of rotten oranges to process in this time unit
            for i in range(length):  # Process each orange in the queue
                r, c = q.popleft()  # Get the current rotten orange's position

                # Check all 4 neighboring cells
                for dr, dc in directions:
                    row, col = r + dr, c + dc  # Calculate the neighboring cell's position
                    # If the neighboring cell is within bounds and contains a fresh orange
                    if (row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2  # Mark the fresh orange as rotten
                        q.append((row, col))  # Add its position to the queue
                        fresh -= 1  # Decrease the count of fresh oranges

            # Increment the time after processing all rotten oranges for this time unit
            time += 1

        # If all fresh oranges are rotten, return the time taken; otherwise, return -1
        return time if fresh == 0 else -1
