class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        m = defaultdict(int)
        ans = 0
        sum = 0
        l,r=0,0
        while r<len(nums):
            if nums[r] not in m or m[nums[r]]<l:
                sum += nums[r]
                m[nums[r]] = r
                r += 1
                ans = max(ans,sum)
            else:
                sum -= nums[l]
                l += 1 
           # print(l,r,ans,sum)
        return ans