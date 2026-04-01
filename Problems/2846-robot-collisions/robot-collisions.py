class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        ans = []
        arr = []

        for i in range(n):
            a,b,c = positions[i],0 if directions[i]=='L' else 1, i
            arr.append([a,b,c])
        arr.sort()
      #  print(arr)
        s = []
        
        for a,b,c in arr:
            if b==0:
                while s and healths[s[-1]] < healths[c]:
                    s.pop()
                    healths[c] -= 1
                if not s:
                    if healths[c]>0:
                        ans.append(c)
                elif healths[s[-1]] == healths[c]:
                    s.pop()
                else:
                    healths[s[-1]] -= 1
                    

            else:
                s.append(c)
           # print(s)
       # print(ans,s)
        for a in s:
            ans.append(a)
      #  print(ans)
        return [healths[x] for x in sorted(ans) if healths[x]>0]


        
        

        