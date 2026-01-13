class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total = 0
        diff = defaultdict(int)
        for _, y, s in squares:
            total += s * s
            diff[y] += s
            diff[y + s] -= s
        area = 0
        target = 0
        for y, y2 in pairwise(sorted(diff)):
            target += diff[y]
            area += target * (y2 - y)
            if area * 2 >= total:
                return y2 - (area * 2 - total) / (target * 2)