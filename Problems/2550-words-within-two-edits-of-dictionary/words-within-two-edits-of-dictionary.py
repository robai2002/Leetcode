class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        n = len(queries[0])
        f = lambda x,y: sum(x[i]!=y[i] for i in range(n))<3
        ans = []
        for word in queries:
            for ck in dictionary:
                if f(word,ck):
                    ans.append(word)
                    break
        return ans