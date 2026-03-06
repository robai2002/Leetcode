class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        c = Counter(bulbs)
        return sorted([x for x,y in c.items() if y%2==1])