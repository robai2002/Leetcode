class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        l = []
        for num in nums:
            l.append(num)
            while len(l)>1 and l[-1] == l[-2]:
                l.pop()
                l[-1]*=2
        return l