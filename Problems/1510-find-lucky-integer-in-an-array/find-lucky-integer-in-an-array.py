class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = -1
        for x,y in Counter(arr).items():
            if x==y:
                ans = max(x,ans)
        return ans
