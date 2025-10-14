class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        c = 0
        ans = 0
        prev = -10000
        for num in nums:
            if num>prev:
                c +=1
            else:
                ans = int(c>=k)
                c = 1
            if c==2*k or ans +c//k>1:
                return True
            prev = num
            #print(num,c)
        #print(ans,c)
        ans += int(c>=k)
        return ans>1


        