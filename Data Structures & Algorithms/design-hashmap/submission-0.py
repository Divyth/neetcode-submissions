class MyHashMap:

    def __init__(self):
        self.capacity = 1000
        self.buckets = [[] for _ in range(self.capacity)]

    def hash(self, key):
        return key % self.capacity

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        bucket = self.buckets[index]

        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return 
        bucket.append([key, value])

    def get(self, key: int) -> int:
        index = self.hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)
        bucket = self.buckets[index]

        for i, (k,v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return 


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)