class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def dfs(i):
            if not(0<=i<len(arr)) or arr[i]==-1:
                return False
            if arr[i]==0:
                return True
            temp=arr[i]
            arr[i]=-1
            return dfs(i+temp) or dfs(i-temp)
        return dfs(start)