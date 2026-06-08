class TimeMap:

    def __init__(self):
        self.map = {} # is the map of string : [[]] ie List of list [[value, timestamp]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.map.get(key, [])

        l = 0
        r = len(values) - 1

        while l <= r:
            m = l + (r-l) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1

            else:
                r = m - 1

        return res
        
