class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(len(nums)):
            mp = dict()
            odd_even = 0
            for j in range(i,n):
                if nums[j] not in mp:
                    mp[nums[j]] = 1
                    if nums[j]%2==0:
                        odd_even -=1
                    else: 
                        odd_even +=1 
                if odd_even ==0:ans = max(ans,j-i+1)
                
        return ans
                
                
                
            
        