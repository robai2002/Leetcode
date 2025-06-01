class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        x = 1
        for v in nums:
            x *= v
        if target*target != x:
            return False
       
        def dfs(ind: int,need: int) ->bool:
            if need == 1:
                return True
            if ind == len(nums):
                return False
            if  need%nums[ind]:
                return dfs(ind+1,need)
            return dfs(ind+1,need//nums[ind]) or dfs(ind+1,need)
        
        return dfs(0,target)