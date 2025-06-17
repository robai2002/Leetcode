class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        sum = 0
        for v in machines:
            sum += v
        if sum%len(machines):
            return -1
        
        sum//=len(machines)
        ans = 0
        x = 0
        b = True
        for i,v in enumerate(machines):
            if x<0 and x+v-sum>0:
                ans = max(ans,abs(x-(x+v-sum)))
            x += v-sum
            ans = max(ans,abs(x))
        return ans
