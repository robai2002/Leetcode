class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        S, T = Counter(s),Counter(target)
        n = len(target)
        st = sorted(set(s))
        ans = -1
        col = ""
        
        for ind,ch in enumerate(target):
            d = bisect.bisect_right(st, ch)
            
            if d<len(st):
                ans= ind
                col =st[d]
            if ch not in st:break
            S[ch] -=1
            if S[ch] ==0:
                st.remove(ch)
    
        if ans ==-1:
            return ""
        final = ""
        S =Counter(s)
        for i in range(ans):
            final += target[i]
            S[target[i]] -= 1
        final += col
        S[col] -= 1
        #print(ans,col,final)
        z = []
        
        for key,value in S.items():
            for i in range(value):
                z.append(key)
        z.sort()
        return final + "".join(z)
        
            
        
            