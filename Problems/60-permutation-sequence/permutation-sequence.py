class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        l = []
        mp = [True for i in range(n+1)]
        x = 1 
        for i in range(1,n):
            x *= i
        for _ in reversed(range(n)):
            c = (k+x-1)//x
            #print(c,x,k)
            k = (k-1)%x+1
            if _:
                x//=_
            ind = 0 
            while c>0:
                ind += 1
                if mp[ind]:
                    c -= 1 
            mp[ind] = False
            l.append(str(ind))
        return "".join(l)