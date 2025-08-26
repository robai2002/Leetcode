class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        digonal =0.0
        area = 0
        for l,b in dimensions:
            if l*l+b*b>digonal:
                digonal = l*l+b*b
                area  = l*b
            elif l*l+b*b==digonal:
                area = max(area,l*b)
        return area