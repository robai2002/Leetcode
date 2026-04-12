class Solution:
    def minimumDistance(self, word: str) -> int:
        @cache 
        def DP(ind, f1, f2) -> int:
            if ind == len(word):return 0

            best = inf
            ch = word[ind]
            pos = ord(ch) - ord('A')
            i,j= divmod(pos,6)

            d1 = 0 if f1 == (-1,-1) else abs(f1[0] - i) + abs(f1[1]-j)
            best = min(best,d1 + DP(ind+1,(i,j),f2))

            d2 = 0 if f2 == (-1,-1) else abs(f2[0] - i) + abs(f2[1]-j)
            best = min(best,d2 + DP(ind+1, f1, (i,j)))
            print(ind,best)

            return best

        return DP(0,(-1,-1),(-1,-1))
        