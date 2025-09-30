class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        lt = len(s)

        while lt >k:
            ss = ''
            start_ind = 0
            end_pos = start_ind+k

            while start_ind<lt:
                substr = s[start_ind:end_pos]
                sum_digits = sum(int(d) for d in substr)
                ss +=  str(sum_digits)
                start_ind +=k
                end_pos+=k
            s = ss
            lt = len(s)
        return s