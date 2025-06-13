class Solution:
    def minimizeMax(self, a: List[int], p: int) -> int:
        pos,amb = -1,max(a)
        a.sort()
        n = len(a)
        while pos<amb:
            dis = (pos+amb+1)//2
            i,c=1,0
            while i<n:
                if a[i]-a[i-1]<=dis:
                    c+= 1
                    i += 1
                i += 1
            print(dis,c)
            if c<p:
                pos = dis
            else:
                amb = dis - 1
        return pos + 1
