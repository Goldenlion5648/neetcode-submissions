class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = Counter()
        goal = Counter(s1)
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            window[s2[i]] += 1

        pos = len(s1)
        while True:
            if window == goal:
                return True
            key = s2[pos-len(s1)]
            window[key] -= 1
            if window[key] == 0:
                window.pop(key)
            if pos == len(s2):
                break
            window[s2[pos]] += 1
            pos += 1
        return False
        
