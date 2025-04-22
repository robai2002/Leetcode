class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp ={}

        def backtracking(ind: int,need: int) ->int:
            if ind == len(nums) :
                return need == 0
            if (ind,need) in dp:
                return dp[(ind,need)]
            dp[(ind,need)] = backtracking(ind+1,need - nums[ind]) + backtracking(ind+1, need + nums[ind])
            return dp[(ind,need)]
        return backtracking(0,target)