class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_rem = sum(x == "R" for x in senate)
        d_rem = sum(x == "D" for x in senate)
        r_skips = 0
        d_skips = 0
        pos = 0
        while r_rem and d_rem:
            if senate[pos] == "R":
                if r_skips > 0:
                    r_skips -= 1
                else:
                    d_skips += 1
                    d_rem -= 1
            else:
                if d_skips > 0:
                    d_skips -= 1
                else:
                    r_skips += 1
                    r_rem -= 1
            pos = (pos + 1) % len(senate)
        if r_rem:
            return "Radiant"
        return "Dire"
