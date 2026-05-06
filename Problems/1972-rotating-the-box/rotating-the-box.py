class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        row = len(boxGrid)
        col = len(boxGrid[0])
        rotate = [["."] * row for _ in range(col)]
        for k, v in enumerate(boxGrid):
            bottom = col - 1
            for j in range(col - 1, -1, -1):
                if v[j] == "#":
                    rotate[bottom][row - 1 - k] = "#"
                    bottom -= 1
                elif v[j] == "*":
                    rotate[j][row - 1 - k] = "*"
                    bottom = j - 1
        return rotate