class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        res = []
        q = deque()

        for i in range(len(nums)):
            # check window size if greater than k remove from left
            while q and q[0] <= i - k:
                q.popleft()

            # check if the last most ie from right of deque is the current greater if so pop from right 
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            
            q.append(i)

            if i >= k - 1:
                res.append(nums[q[0]])

        return res