class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0 
            
        count = 0 
        intervals.sort(key=lambda x:x[1])

        lastend = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < lastend:
                count += 1
            else:
                lastend = intervals[i][1]
        return count
        