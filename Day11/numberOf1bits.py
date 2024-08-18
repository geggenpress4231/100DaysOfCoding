class Solution:
    def hammingWeight(self, n: int) -> int:
        s = format(n, "b") 
        return s.count("1")  