class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0 
        if num1<num2:
            num1,num2 = num2,num1
        while num2:
            ans += num1//num2
            num1,num2 = num2,num1%num2
        return ans
