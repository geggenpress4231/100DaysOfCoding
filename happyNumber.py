class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while True:
            n = self.sumOfSquares(n)
            if n == 1:
                return True
            if n in s:
                return False
            s.add(n)

    def sumOfSquares(self, n: int) -> int:
        total = 0
        while n:
            digit = n % 10
            total += digit * digit
            n //= 10
        return total
