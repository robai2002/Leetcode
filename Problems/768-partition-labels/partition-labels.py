import collections as C
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        x = 0
        y = 0
        m = C.defaultdict(list)
        for i,c in enumerate(s):
            if c in m:
                m[c][1]=i
            else:
                m[c]=[i,i]
        for i,c in enumerate(s):
            if x<i:
                ans.append(i-y)
                y=i
            if x<m[c][1]:
                x= m[c][1]
        ans.append(x-y+1)
        return ans 