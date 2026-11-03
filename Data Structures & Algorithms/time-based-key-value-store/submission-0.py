class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append([timestamp, value])


    def get(self, key: str, timestamp: int) -> str:
        lo = 0
        hi = len(self.cache[key])
        ret = ""
        while lo < hi:
            mid = (lo + hi) // 2
            if self.cache[key][mid][0] <= timestamp:
                ret = self.cache[key][mid][1]
                lo = mid + 1
            else:
                hi = mid
        return ret
        
