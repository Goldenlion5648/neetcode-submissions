class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pre_to_after = defaultdict(set)
        after_to_pre = defaultdict(set)
        num_pointing_into = [0]* numCourses
        for a, b in prerequisites:
            pre_to_after[a].add(b)
            after_to_pre[b].add(a)
            num_pointing_into[b] += 1
        
        fringe = deque()
        for i in range(numCourses):
            if i not in after_to_pre:
                fringe.append(i)

        while fringe:
            cur = fringe.popleft()
            for x in pre_to_after[cur]:
                num_pointing_into[x] -= 1
                after_to_pre[x] |= after_to_pre[cur]
                if num_pointing_into[x] == 0:
                    fringe.append(x)
        
        return [a in after_to_pre[b] for a, b in queries]
                    










                            
                    