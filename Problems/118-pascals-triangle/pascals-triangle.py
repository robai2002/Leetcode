class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(numRows-1):
            l = ans[-1].copy()
            ans.append([])
            for ind,v in enumerate(l,start =-1):
                if ind<0:
                    ans[-1].append(v)
                else:
                    ans[-1].append(v+l[ind])
            ans[-1].append(1)
        return ans
                    