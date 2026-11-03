class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.vals = nums
        heapq.heapify(self.vals)
        self.k = k
        while len(self.vals) > k:
            heapq.heappop(self.vals)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.vals, val)
        if len(self.vals) > self.k:
            heapq.heappop(self.vals)
        return self.vals[0]

        
