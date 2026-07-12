from sortedcontainers import SortedSet

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s = SortedSet(arr)
        mp = dict()
        for ind,val in enumerate(s,1):
            mp[val] = ind
        return [mp[num] for num in arr]
        