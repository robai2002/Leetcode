class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        x,y=0,0
        for ch in word:
            if not ch.isalnum():
                return False
            if ch.isalpha():
                if ch.lower() in "aeiou":
                    x+= 1
                else:
                    y+=1
        return x>0 and y>0