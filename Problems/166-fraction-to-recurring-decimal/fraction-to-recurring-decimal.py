class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator ==0:
            return "0"
        ans =""
        if (numerator < 0) ^ (denominator < 0):
            ans += "-" 
        numerator, denominator = abs(numerator) , abs(denominator)

        ans += str(numerator//denominator)
        rmd = numerator%denominator

        if rmd ==0:return ans
        ans+='.'

        remainder_dict = {}
        
        while rmd!=0 and rmd not in remainder_dict:
            remainder_dict[rmd] = len(ans)
            rmd*=10
            ans += str(rmd//denominator)
            rmd %= denominator

        
        if rmd in remainder_dict:
            ans = ans[:remainder_dict[rmd]] + "(" + ans[remainder_dict[rmd]:] + ")"
        return ans


