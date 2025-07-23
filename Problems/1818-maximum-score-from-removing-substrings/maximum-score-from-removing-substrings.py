class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        def remove_pairs(pair,score):
            nonlocal s
            res = 0
            stack = []
            for c in s:
                if c == pair[1] and stack and stack[-1] == pair[0]:
                    stack.pop()
                    res += score
                else:
                    stack.append(c)
            s = "".join(stack)
            return res
        
        if x>y:
            a,b = "ab","ba"
        else:
            b,a = "ab","ba"
            x,y= y,x
        res = 0
        res  += remove_pairs(a,x)
        res += remove_pairs(b,y)

        return res