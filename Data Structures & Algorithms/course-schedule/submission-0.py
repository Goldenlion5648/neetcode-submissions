'''
check courses that are not in the prereqs

'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = Counter()
        pre_to_afters = defaultdict(list)

        for after, pre in prerequisites:
            pre_to_afters[pre].append(after)
            in_degree[after] += 1
        
        fringe = []
        for i in range(numCourses):
            if i not in in_degree:
                fringe.append(i)
        
        while fringe:
            cur = fringe.pop()
            for after in pre_to_afters[cur]:
                in_degree[after] -= 1
                if in_degree[after] == 0:
                    fringe.append(after)
                    in_degree.pop(after)
        return len(in_degree) == 0








