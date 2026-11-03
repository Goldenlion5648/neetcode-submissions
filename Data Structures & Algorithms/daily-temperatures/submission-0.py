'''
[30,38,30,36,35,40,28]
 28,30,30,35,36,38,40

 4 6 7 9


 4 

 1

9 6 4 3 2 4


9 6 4 3
      2 1
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ret = [0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            while len(stack) and temp > stack[-1][0]:
                old_day = stack[-1][1]
                ret[old_day] = i - old_day
                stack.pop()
            stack.append((temp, i))
        return ret




