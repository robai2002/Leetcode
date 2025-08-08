class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        n = len(nums)

        if n == 1:
            return abs(nums[0]-24) <0.001
        
        for i in range(n):
            for j in range(i+1,n):
                c1 = nums[i]
                c2 = nums[j]
                possres = [c1+c2,c1-c2,c2-c1,c1*c2]
                if c1:
                    possres.append(c2/c1)
                if c2:
                    possres.append(c1/c2)
                
                nextcard = [nums[k] for k in range(n) if k not in {i,j}]
                for v in possres:
                    nextcard.append(v)
                    if self.judgePoint24(nextcard):
                        return True
                    nextcard.pop()
        return False
                    

                     