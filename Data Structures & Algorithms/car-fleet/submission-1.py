class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
    # Step 1: pair position with time
        cars = []
        for p, s in zip(position, speed):
            time = (target - p) / s
            cars.append((p, time))
        
        # Step 2: sort by position DESC
        cars.sort(reverse=True)
        
        stack = []  # stores fleet times
        
        for pos, time in cars:
            # if stack empty OR cannot catch fleet ahead
            if not stack or time > stack[-1]:
                stack.append(time)  # new fleet
            # else: merges → do nothing
        
        return len(stack)