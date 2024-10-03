class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort to handle duplicates
        
        def backtrack(start, subset):
            # Add a copy of the current subset to the result
            res.append(subset.copy())
            
            for i in range(start, len(nums)):
                # If the current number is the same as the previous one, skip it to avoid duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                # Include nums[i] in the subset and move to the next element
                subset.append(nums[i])
                backtrack(i + 1, subset)
                
                # Backtrack by removing the last element added
                subset.pop()
        
        backtrack(0, [])
        return res
