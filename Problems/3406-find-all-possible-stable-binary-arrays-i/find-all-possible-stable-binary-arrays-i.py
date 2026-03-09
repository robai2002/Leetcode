class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = int(1e9) + 7
        
        @cache
        def recursive(zeroleft,onesleft,prev):

            if zeroleft == 0 and  onesleft == 0 : return 1

            res = 0

            if prev != 0:
                for i in range(1,min(limit,zeroleft)+1):
                    res += recursive(zeroleft-i,onesleft,0)
                    res %= mod
           
            if prev != 1:
                for i in range(1,min(limit,onesleft)+1):
                    res += recursive(zeroleft,onesleft-i,1)  
                    res %= mod     
            
            return res % mod
            
        
        return recursive(zero,one,-1)
