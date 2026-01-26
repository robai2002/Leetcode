class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = 10**9
        for x,y in pairwise(arr):
            ans = min(ans,y-x)
        return [[x,y] for x,y in pairwise(arr) if y-x==ans]
        