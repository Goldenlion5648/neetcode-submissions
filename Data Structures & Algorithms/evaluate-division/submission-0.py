class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        top_to_bottom_to_mult = defaultdict(dict)

        for val, (a, b) in zip(values, equations):
            top_to_bottom_to_mult[a][b] = val
            top_to_bottom_to_mult[b][a] = 1.0 / val
        
        ret = []
        for a, b in queries:
            if a not in top_to_bottom_to_mult or b not in top_to_bottom_to_mult:
                ret.append(-1)
                continue
            fringe = deque()
            fringe.append((a, 1))
            seen = set()
            found = False
            while fringe:
                cur, mult = fringe.pop()
                if cur in seen:
                    continue
                seen.add(cur)
                if cur == b:
                    ret.append(mult)
                    found = True
                    break
                for bottom in top_to_bottom_to_mult[cur]:
                    fringe.append((bottom, mult * top_to_bottom_to_mult[cur][bottom]))
            if not found:
                ret.append(-1)
        return ret

