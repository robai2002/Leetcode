from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        graph = [['.'for i in range(n)] for _ in range(n)]
        col = set()
        pos = set()
        neg = set()
        ans = []
        def helper(graph,ind: int) -> None:
            if ind == n:
                ans.append([''.join(x) for x in graph])
                return 
            for i in range(n):
                if i not in col:
                    if (ind+i) not in pos:
                        if ind-i not in neg:
                            graph[ind][i] = 'Q'
                            pos.add(i+ind)
                            neg.add(ind - i)
                            col.add(i)
                            helper(graph,ind+1)
                            graph[ind][i] ='.'
                            pos.remove(i+ind)
                            neg.remove(ind - i)
                            col.remove(i)
            return
        helper(graph,0)

        return ans