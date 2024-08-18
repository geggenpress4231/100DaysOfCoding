from collections import defaultdict
from typing import List

class DetectSquares:

    def __init__(self):
        self.point_count = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.point_count[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        square_count = 0
        
        for (x3, y3), count in self.point_count.items():
            if abs(x1 - x3) == 0 or abs(x1 - x3) != abs(y1 - y3):
                continue
            square_count += count * self.point_count.get((x1, y3), 0) * self.point_count.get((x3, y1), 0)
        
        return square_count
