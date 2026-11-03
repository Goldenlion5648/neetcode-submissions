class MyHashMap:

    def __init__(self):
        self.map = [[] for _ in range(100_000)]
        self.mod = 99_991

    def put(self, key: int, value: int) -> None:
        hashed = key % self.mod
        for i, (old_key, old_val) in enumerate(self.map[hashed]):
            if old_key == key:
                self.map[hashed][i][1] = value
                return
        self.map[hashed].append([key, value])

    def get(self, key: int) -> int:
        hashed = key % self.mod
        for i, (old_key, old_val) in enumerate(self.map[hashed]):
            if old_key == key:
                return old_val
        return -1

    def remove(self, key: int) -> None:
        hashed = key % self.mod
        for i, (old_key, old_val) in enumerate(self.map[hashed]):
            if old_key == key:
                self.map[hashed][i], self.map[hashed][-1] = self.map[hashed][-1], self.map[hashed][i]
                self.map[hashed].pop()
                break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)