class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if self.right and num > self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush_max(self.left, num)
        if len(self.left) - len(self.right) >= 2:
            left_highest = heapq.heappop_max(self.left)
            heapq.heappush(self.right, left_highest)
        if len(self.right) - len(self.left) >= 2:
            right_lowest = heapq.heappop(self.right)
            heapq.heappush_max(self.left, right_lowest)

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (self.left[0] + self.right[0]) / 2
        if len(self.left) > len(self.right):
            return self.left[0]
        return self.right[0]
        
        