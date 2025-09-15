class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans = 0
        x = 0
        for c in text:
            if c == ' ':
                if x==0:
                    ans += 1
                x = 0
            elif c in brokenLetters:
                x = 1
        
        return ans+1-x

        