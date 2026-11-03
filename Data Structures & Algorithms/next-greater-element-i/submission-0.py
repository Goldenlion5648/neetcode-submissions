class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        num_to_higher = {}
        for x in nums2:
            if not stack or stack[-1] > x:
                stack.append(x)
            else:
                #new num is higher than previous
                while stack and stack[-1] < x:
                    num_to_higher[stack[-1]] = x
                    stack.pop()
                stack.append(x)
        
        ret = []
        for x in nums1:
            if x not in num_to_higher:
                ret.append(-1)
            else:
                ret.append(num_to_higher[x])
        return ret