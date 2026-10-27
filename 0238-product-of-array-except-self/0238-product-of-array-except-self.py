class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        left, right = [1] * len(nums), [1] * len(nums)

        for i in range(1, length):
            left[i] = nums[i-1] * left[i-1]

        for i in range(length-2, -1, -1):
            right[i] = nums[i+1] * right[i+1]
        
        for i in range(length):
            nums[i] = left[i] * right[i]
        
        return nums