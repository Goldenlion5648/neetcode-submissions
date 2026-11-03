class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        ret = [0]*len(temps)
        for i, ele in enumerate(temps):
            while stack and ele > stack[-1][1]:
                old_i, old_temp = stack.pop()
                ret[old_i] = i - old_i            
            stack.append((i, ele))
        return ret