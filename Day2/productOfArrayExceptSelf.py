class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [1] * length

     
        for i in range(1, length):
            answer[i] = answer[i - 1] * nums[i - 1]

       
        right_product = 1
        for i in range(length - 1, -1, -1):
            answer[i] = answer[i] * right_product
            right_product *= nums[i]

        return answer
