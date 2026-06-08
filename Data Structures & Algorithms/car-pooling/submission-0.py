class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []

        for delta, s , e in trips:
            events.append((s, delta))
            events.append((e, -delta))
        
        events.sort(key= lambda x:(x[0], x[1]))

        current = 0
        for _, delta in events:
            current += delta
            if current > capacity:
                return False
        return True

        