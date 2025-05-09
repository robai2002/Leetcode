class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        part = []
        def isValid(i: int,j: int) -> bool:
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1;j-=1
            return True


        def dfs(ind: int) -> None:
            print(ind,part)
            if ind == len(s):
                ans.append(part.copy())
                return 
            for i in range(ind,len(s)):
                if isValid(ind,i):
                    part.append(s[ind:i+1])
                    dfs(i+1)
                    part.pop()
            return 

        dfs(0)
        return ans