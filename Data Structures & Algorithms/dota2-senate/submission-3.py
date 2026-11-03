class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d_rem = sum(x == "D" for x in senate)
        r_rem = sum(x == "R" for x in senate)
        r_skips = 0
        d_skips = 0
        senate_q = deque(senate)
        while r_rem and d_rem:
            if senate_q[0] == "R":
                if r_skips > 0:
                    senate_q.popleft()
                    r_rem -= 1
                    r_skips -= 1
                else:
                    d_skips += 1
                    senate_q.rotate(-1)
            else:
                if d_skips > 0:
                    senate_q.popleft()
                    d_rem -= 1
                    d_skips -= 1
                else:
                    r_skips += 1
                    senate_q.rotate(-1)

        if r_rem:
            return "Radiant"
        return "Dire"
