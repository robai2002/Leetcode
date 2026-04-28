class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        i,n,ans = 0,len(instructions),0
        while 0<=i<n and instructions[i]!='done':
            if instructions[i]=='add':
                ans += values[i]
                instructions[i] = 'done'
                i += 1
            else:
                instructions[i] = 'done'
                i += values[i]
        return ans
        