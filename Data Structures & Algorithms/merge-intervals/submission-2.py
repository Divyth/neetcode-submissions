class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]: 
        res = []
        intervals.sort(key = lambda x: x[0])

        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                end = max(intervals[i][1], end)
            else:
                res.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
        res.append([start,end])
        return res