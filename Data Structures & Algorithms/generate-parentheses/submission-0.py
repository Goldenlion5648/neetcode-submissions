class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        fringe = deque([("", 0)])
        ret = []
        while fringe:
            cur_string, depth = fringe.pop()
            if depth > len(cur_string) or len(cur_string) > n * 2 or depth < 0:
                continue
            if depth == 0 and len(cur_string) == n*2:
                ret.append(cur_string)
                continue
            depth_to_add = 1
            for symbol in "()":
                fringe.append((cur_string + symbol, depth + depth_to_add))
                depth_to_add = -1
        return ret