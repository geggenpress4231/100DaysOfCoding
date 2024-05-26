
class Solution:
    def maxSubArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n < k:
            return "Invalid input"
        
        max_sum = float('-inf')
        current_sum = 0
        left = 0
        
        for right in range(n):
            current_sum += nums[right]
            
            # If window size exceeds k, shrink the window from the left
            if right - left + 1 > k:
                current_sum -= nums[left]
                left += 1
            
            # Update max_sum if we have a valid window size
            if right - left + 1 == k:
                max_sum = max(max_sum, current_sum)
        
        return max_sum