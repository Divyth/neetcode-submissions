class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for task in tasks:
            # if task in count:
            #     count[task] += 1
            # else:
            #     count[task] = 1
            count[task] = count.get(task,0) + 1
        # we can also use count = Counter(tasks) built in 

        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        q = deque() # we store(-cnt, iddleTime)
        time = 0
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap) # +1 to reduce the count since count is in negative(maxHEap)

                if cnt: # if cnt is non null
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time: # if the task queue is available at time ie after waiting 
                heapq.heappush(maxHeap, q.popleft()[0])
        return time



        