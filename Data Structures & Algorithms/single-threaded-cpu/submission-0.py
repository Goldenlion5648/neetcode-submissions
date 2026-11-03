from _heapq import heappop
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        order = []
        tasks = [(start, length, i) for i, (start, length) in enumerate(tasks)]
        tasks.sort()
        ret = []
        process_until_time = tasks[0][0]
        pos = 0
        while len(ret) < len(tasks):
            ran = False
            while pos < len(tasks) and (tasks[pos][0] <= process_until_time or not ran):
                _, length, old_index = tasks[pos]
                heapq.heappush(order, (length, old_index))
                pos += 1
                ran = True
            lowest = heappop(order)
            process_until_time += lowest[0]
            ret.append(lowest[1])
        return ret


            

