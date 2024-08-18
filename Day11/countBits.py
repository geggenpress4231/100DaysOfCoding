class Solution:
     def countBits(self, n: int) -> List[int]:
        bitList = []
        for i in range(0, n + 1):
            s = format(i, "b")
            bitList.append(s.count('1'))  
        return bitList   

        