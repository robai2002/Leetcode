class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        indP,indN,n = 0,1,len(nums)
        ans = [0]*n
        for num in nums:
            if num<0:
                ans[indN] = num
                indN += 2
            else:
                ans[indP] = num
                indP += 2
        return ans

        