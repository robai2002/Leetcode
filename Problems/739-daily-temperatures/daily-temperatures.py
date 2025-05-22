class Solution:
    def dailyTemperatures(self, tmp: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(tmp)
        for i,val in enumerate(tmp):
            while stack and stack[-1][1]<val:
                index,value = stack.pop()
                ans[index] =  i - index
            stack.append([i,val])      
        return ans 