class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhat(p1, p2):
            return sum(abs(coord1 - coord2) for coord1, coord2 in zip(p1, p2))
        connected = [False]*len(points)
        connected[0] = True
        connected_size = 1
        distances = [math.inf]*len(points)
        newest = 0
        ret = 0
        while connected_size < len(points):
            cur_dist = math.inf
            pos_to_use = None
            for i in range(len(points)):
                if connected[i]:
                    continue
                cur_dist = manhat(points[newest], points[i])
                distances[i] = min(distances[i], cur_dist)
                if pos_to_use is None or distances[i] < distances[pos_to_use]:
                    pos_to_use = i

            ret += distances[pos_to_use]
            newest = pos_to_use
            connected[pos_to_use] = True
            connected_size += 1
        return ret