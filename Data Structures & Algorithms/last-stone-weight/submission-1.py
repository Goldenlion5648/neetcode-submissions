class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            largest = heapq.heappop_max(stones)
            second = heapq.heappop_max(stones)
            if largest == second:
                continue
            heapq.heappush_max(stones, (largest-second))
            
        if not stones:
            return 0
        return stones[0]