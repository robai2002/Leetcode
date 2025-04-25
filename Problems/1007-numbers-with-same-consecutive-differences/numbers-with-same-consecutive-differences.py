class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return [i for i in range(10)]
        q = [digit for digit in range(1,10)]
        for level in range(n - 1):
            next_q = []
            for num in q:
                tail_digit = num % 10 
                next_digits = set([tail_digit - k, tail_digit + k])
                for next_digit in next_digits:
                    if 0 <= next_digit < 10:
                        new_num = num * 10 + next_digit
                        next_q.append(new_num)
            q = next_q 
        return q