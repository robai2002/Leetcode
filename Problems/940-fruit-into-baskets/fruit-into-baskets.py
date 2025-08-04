class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        x,y=-1,-1
        a,b=-1,-1
        s = -1
        c,ans =0,0
        for i,fruit in enumerate(fruits):
            if fruit==x:
                a = i
            elif fruit==y:
                b = i
            elif a<b:
                s = a 
                a = i
                x = fruit
            else:
                s = b
                b = i
                y = fruit
        
            ans = max(ans,i-s)
        
        return ans
        