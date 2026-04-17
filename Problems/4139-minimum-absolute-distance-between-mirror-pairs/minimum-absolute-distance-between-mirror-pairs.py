class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:

        def rev(x: int) -> int:
            y = 0
            while x:
                y = y*10 + x%10
                x//=10
            return y
        
        ans,n = len(nums), len(nums)
        mp = dict()
        for ind,num in enumerate(nums,start = 1):
            ans = min(ans,ind - mp.get(num,-n))
            num = rev(num)
            # print(nums[ind-1],num,mp.get(nums[ind-1],-n))
            mp[num] = ind
        return ans if ans<n else -1