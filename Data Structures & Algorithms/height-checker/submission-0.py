class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counts = [0]*101
        for i in range(len(heights)):
            counts[heights[i]] += 1
        
        expected = []
        for i in range(len(counts)):
            for j in range(counts[i]):
                expected.append(i)
        
        ret = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                ret += 1
        return ret
