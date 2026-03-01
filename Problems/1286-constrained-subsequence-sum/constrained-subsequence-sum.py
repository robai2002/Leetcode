class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        q = []
        heappush(q,(0,1))
        ans = -10**6
        for ind,num in enumerate(nums):
            while q and k-q[0][1]<ind:
                heappop(q)
            z = num - (q[0][0] if q else 0)
            num = max(z,num)
            ans = max(ans,num)
            heappush(q,(-num,-ind))
        return ans

