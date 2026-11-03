class CountSquares:

    def __init__(self):
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        ret = 0
        #above and below
        for y in range(1001):
            to_find = (point[0], y)
            if y == point[1]:
                continue
            if to_find in self.points:
                diff = y - point[1]
                second = (point[0] - diff, point[1])
                third = (point[0] - diff, point[1] + diff)
                if second in self.points and\
                third in self.points:
                    ret += self.points[to_find] * self.points[second] * self.points[third]
                second = (point[0] + diff, point[1])
                third = (point[0] + diff, point[1] + diff)
                if second in self.points and\
                third in self.points:
                    ret += self.points[to_find] * self.points[second] * self.points[third]
        return ret

