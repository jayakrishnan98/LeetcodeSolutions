class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        length = len(nums)

        left, right = [1] * length, [1] * length
        
        result = []

        for i in range(1,length):
            left[i] = nums[i-1] * left[i-1]


        for i in range(length-2, -1, -1):
            right[i] = nums[i + 1] * right[i + 1]


        for i in range(length):
            result.append(left[i] * right[i])

        return result


