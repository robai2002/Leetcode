class Solution:
    def toGoatLatin(self, sentence: str) -> str:

        words = sentence.split(" ")

        def C(s: str,n: int) ->str:
            ans = []
            if s[0].lower() not in "aeiou":
                return s[1:] + s[0] + "ma" + 'a'*n
            else:
                return s + "ma" + "a"*n
            
        
        words = [C(word,i+1) for i,word in enumerate(words)]
        return " ".join(words)

        