class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        if n&1:
            ans.append(0)
        for i in range(n//2):
            ans.append(i+1)
            ans.append(-ans[-1])
        return ans
            
        