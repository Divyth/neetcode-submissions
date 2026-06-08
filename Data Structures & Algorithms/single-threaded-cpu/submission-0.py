class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i) # beacuse we need to store original indexes

        tasks.sort(key= lambda x:x[0]) # sort according to enqueue time
        res = []
        minHeap = []
        i = 0
        time = tasks[0][0]

        while minHeap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]])
                i += 1
            
            if not minHeap: # if heap is null and the upcoming task is 100 time so instead of waiting untill 100 start from 100 ie assign time = 100
                time = tasks[i][0] 
            
            else:
                processTime, index = heapq.heappop(minHeap)
                res.append(index)
                time += processTime
        return res
            

        