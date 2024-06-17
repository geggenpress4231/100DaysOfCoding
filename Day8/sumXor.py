class Solution:
    def getSum(self, a: int, b: int) -> int:
       
        while b != 0:
            carry = (a & b) & 0xFFFFFFFF  
            a = (a ^ b) & 0xFFFFFFFF 
            b = (carry << 1) & 0xFFFFFFFF  
        
       
        return a if a <= 0x7FFFFFFF else ~(a ^ 0xFFFFFFFF)