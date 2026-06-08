"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
    #     start = sorted([i.start for i in intervals])
    #     end = sorted([i.end for i in intervals])

    #     res = count = 0
    #     s = e = 0

    #     while s < len(intervals):
    #         if start[s] < end[e]:
    #             s += 1
    #             count += 1
                
    #         else:
    #             e += 1
    #             count -= 1
    #         res = max(res, count)
    #     return res


        intervals.sort(key = lambda x:x.start)
        min_heap = []

        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)