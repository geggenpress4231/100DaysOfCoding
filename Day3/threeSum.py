class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break  # optimization: stop if i is positive
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicates
            
            left, right = i + 1, len(nums) - 1
            target = -nums[i]
            
            while left < right:
                _sum = nums[left] + nums[right]
                
                if _sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # skip duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif _sum < target:
                    left += 1
                else:
                    right -= 1
        
        return result
