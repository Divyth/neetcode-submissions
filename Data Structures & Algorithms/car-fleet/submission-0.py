from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Step 1: Create a list of (position, speed) pairs
        pair = [(p, s) for p, s in zip(position, speed)]
        
        # Step 2: Sort the pairs in descending order based on position
        #         (So we process cars from closest to the target first)
        pair.sort(reverse=True)

        # Step 3: Use a stack to track fleet times
        stack = []

        # Step 4: Iterate through sorted cars
        for p, s in pair:  
            # Compute time for each car to reach the target
            time = (target - p) / s  
            stack.append(time)  # Push the time onto the stack

            # Step 5: If the last car (stack[-1]) catches up with the second-last car (stack[-2]),
            #         they form a fleet, so remove the last car from the stack
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        # Step 6: The size of the stack represents the number of fleets
        return len(stack)
