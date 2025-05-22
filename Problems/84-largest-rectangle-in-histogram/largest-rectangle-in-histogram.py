class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = []
        ans = 0

        for i,v in enumerate(heights):
            x = i 
            while l and l[-1][0] >= v:
                _,x = l.pop()
                ans = max(ans,(i-x)*_)
            l.append([v,x])
        while l:
            _,x = l.pop()
            ans = max(ans,(len(heights)-x)*_)
        return ans
        