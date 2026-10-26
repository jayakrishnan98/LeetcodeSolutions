class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n

        left_product = 1
        right_product = 1

        for i in range(n):
            left = i
            right = n - 1 - i

            result[left] *= left_product
            result[right] *= right_product

            left_product *= nums[left]
            right_product *= nums[right]

        return result