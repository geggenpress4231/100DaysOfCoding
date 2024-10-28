class Solution:
    def reverse(self, n: int) -> int:
        int_max, int_min = 2**31, -2**31 -1
        revnum = 0
        if n < 0:
            sign = -1
        else:
            sign = 1
        
        n=abs(n)

        while n>0:
            lastdigit = n%10
            revnum = (revnum*10) + lastdigit

            n=n//10
        result = revnum*sign

        if result > int_max or result < int_min:
            return 0
        else:
            return result