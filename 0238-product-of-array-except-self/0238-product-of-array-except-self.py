class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        length = len(nums)
        result = [1] * length

        for i in range(1, length):
            result[i] = nums[i-1] * result[i-1]
        
        right_product = 1

        for i in range(length-1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        
        
        return result