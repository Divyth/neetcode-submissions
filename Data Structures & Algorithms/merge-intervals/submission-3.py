class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]: 
        res = []
        intervals.sort(key = lambda x: x[0])

        # start = intervals[0][0]
        # end = intervals[0][1]
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            if  intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(intervals[i][1], res[-1][1])
            else:
                res.append(intervals[i])
                # start = intervals[i][0]
                # end = intervals[i][1]
        
        return res