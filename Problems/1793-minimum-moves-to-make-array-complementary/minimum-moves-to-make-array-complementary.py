class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0 for  i in range(limit*2+2)]
        for i in range(n//2):
            a,b = min(nums[i],nums[n-i-1]), max(nums[i],nums[n-i-1])
            
            diff[a+1] -= 1
            diff[b+limit+1] += 1

            diff[a+b] -=1
            diff[a+b+1] += 1 

            diff[2] += 2
            diff[limit*2+1] -= 2
        ans = n
    
    
        for i in range(2,limit*2+1):
            diff[i] += diff[i-1]
            ans = min(ans,diff[i])
  
        return ans


        