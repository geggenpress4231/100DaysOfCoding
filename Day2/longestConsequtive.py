from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        max_len = 1  
        current_len = 1  

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue  
            elif nums[i] == nums[i - 1] + 1:
                current_len += 1
            else:
                max_len = max(max_len, current_len) 
                current_len = 1  

        max_len = max(max_len, current_len)  
        return max_len
#aliter better
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
