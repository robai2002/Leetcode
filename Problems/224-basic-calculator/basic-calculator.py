class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        cur_num, sign, res = 0, 1, 0

        for c in s:
            if c.isdigit():
                cur_num *= 10
                cur_num += int(c)

            elif c == '+' or c == '-':
                res += cur_num * sign 

                sign = -1 if c == '-' else 1
                cur_num = 0

            elif c == '(':
                stack.append(res)
                stack.append(sign)

                res, sign = 0, 1

            elif c == ')':
                res += sign * cur_num

                res *= stack.pop()
                res += stack.pop()
                cur_num = 0

        return res + cur_num * sign