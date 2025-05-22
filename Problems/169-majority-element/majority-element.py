#boyer and moore majority vote Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #moore voting algorithm 
        x,cnt=0,0
        for v in nums:
            if cnt == 0:
                x = v
            if v==x:
                cnt += 1
            else:
                cnt -= 1
        return x