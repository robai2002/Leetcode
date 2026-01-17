class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        ans = 0 
        for i,(l,r) in enumerate(zip(bottomLeft,topRight)):
            for (m,n) in zip(bottomLeft[i+1:],topRight[i+1:]):
                x = min(r[0], n[0]) - max(l[0], m[0])
                y = min(r[1], n[1]) - max(l[1], m[1])
                ans= max(ans,min(x,y))
                
                
        return ans*ans

                    

            
