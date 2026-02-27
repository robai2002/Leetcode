class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        s = str(n)
        ans = 0
        x = 9
        for i in range(len(s)-1):
            ans += x
            x *= (9-i)
        st = set()
        ln = len(s)
        z = 1
        for i in range(ln-1):z *= (9-i)
        
        for ind,ch in enumerate(s):
            
            p = ord(ch)
            if ind>0:
                for ch1 in range(ord('0'),p):
                    if chr(ch1) not in st:
                        ans += z
            else:
                ans += (p-49)*z
            #print(ind,ch,p,z,ans)
            if ch in st:
                return n-ans
            z//= (9-ind)
            st.add(ch)
            if len(s) == len(st):
                # print(len(s),len(st),s,st)
                ans+= 1
        
        # for ch in range(ord('0'),ord(s[-1])+1):
        #     if chr(ch) not in st:
        #         ans+= 1
        # if len(s)==1:
        #     ans-=1




        return n-ans
        
        