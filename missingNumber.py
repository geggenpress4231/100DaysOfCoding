class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (lambda arr, n: (n * (n + 1)) // 2 - sum(arr))(nums, n)
