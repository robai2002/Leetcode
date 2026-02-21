class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime = [2, 3, 5, 7, 11, 13, 17, 19]
        a = [i for i in range(left,right+1)]
        count = 0
        for i in a:
            b = bin(i)[2:]
            if b.count('1') in prime:
                count += 1
        return count