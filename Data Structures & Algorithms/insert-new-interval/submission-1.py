class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for interval in intervals:
            # if current interval before the newInterval, means current intervals end is less than the new intervals start time
            if interval[1] < newInterval[0]:
                res.append(interval)

                # if current interval after the newInterval, means current intervals start time is greater than the new intervals end time
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                newInterval = interval # move forward

            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        res.append(newInterval)
        return res

        
        