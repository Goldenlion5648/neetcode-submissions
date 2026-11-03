import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # key (abs, x - ele)
        closest = []
        for ele in arr: # 2
            # [(4, 4), (2, 2), (1, 1)]
            heapq.heappush_max(closest, (abs(ele - x), ele - x, ele))
            if len(closest) > k:
                heapq.heappop_max(closest)
        return sorted([val for _, _, val in closest])
