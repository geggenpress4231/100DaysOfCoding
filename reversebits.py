class Solution:
    def reverseBits(self, n: int) -> int:
        return int(f'{n:032b}'[::-1], 2)



class Solution:
    def reverseBits(self, n: int) -> int:
            
        result = 0
        for i in range(32):
            # Shift result to the left to make space for the next bit
            result <<= 1
            # Add the least significant bit of n to result
            result |= (n & 1)
            # Shift n to the right to get the next bit
            n >>= 1
        return result

        