class Solution:
    def trap(self, h: List[int]) -> int:
        i = 0
        j= len(h) - 1
        left = 0
        right =0 
        ans = 0
        while i <= j:
            if left < right:
                if h[i] < left:
                    ans +=left-h[i]
                else:
                    left = h[i]
                i += 1
            elif h[j] <right:
                ans += right - h[j]
                j -= 1
            else :
                right = h[j]
                j -= 1
        return ans