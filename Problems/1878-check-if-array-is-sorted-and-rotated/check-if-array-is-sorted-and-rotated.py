class Solution:
    def check(self, nums: List[int]) -> bool:
        s,n = 1,len(nums) 
        nums.extend(nums[:-1])
        for num1,num2 in pairwise(nums):
            if num1>num2:s = 0
            s += 1
            if n==s:return True
        
        return n==s
        