class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            largest = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            if largest == second:
                continue
            heapq.heappush(stones, -(largest-second))
            
        if not stones:
            return 0
        return -heapq.heappop(stones)