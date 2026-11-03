class CountSquares:

    def __init__(self):
        self.points = Counter()
        

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        ret = 0
        for existing in self.points:
            x_diff = point[0] - existing[0]
            y_diff = point[1] - existing[1]
            if abs(x_diff) == abs(y_diff) and abs(x_diff) > 0:
                left = (point[0] - x_diff, point[1])
                above = (point[0], point[1] - y_diff)
                if left in self.points and above in self.points:
                    ret += self.points[existing] * self.points[left] * self.points[above]
        return ret

