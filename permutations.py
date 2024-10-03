

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         def backtrack(first = 0):
#             # if all integers are used up
#             if first == n:
#                 output.append(nums[:])
#             for i in range(first, n):
#                 # place i-th integer first in the current permutation
#                 nums[first], nums[i] = nums[i], nums[first]
#                 # use next integers to complete the permutations
#                 backtrack(first + 1)
#                 # backtrack
#                 nums[first], nums[i] = nums[i], nums[first]

#         n = len(nums)
#         output = []
#         backtrack()
#         return output




class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(current):
            # Base case: if the current permutation is the same length as nums
            if len(current) == len(nums):
                res.append(current.copy())
                return
            
            # Recursive case: iterate through all numbers and build permutations
            for num in nums:
                if num not in current:
                    current.append(num)
                    dfs(current)
                    current.pop()
        
        dfs([])
        return res
