class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        counts = Counter(s1)
        big_counts = Counter()
        for i in range(len(s1)):
            big_counts[s2[i]] += 1
        if counts == big_counts:
            return True

        for i in range(len(s1), len(s2)):
            big_counts[s2[i-len(s1)]] -= 1
            if big_counts[s2[i-len(s1)]] == 0:
                big_counts.pop(s2[i-len(s1)])
            big_counts[s2[i]] += 1
            if counts == big_counts:
                return True
        return False
