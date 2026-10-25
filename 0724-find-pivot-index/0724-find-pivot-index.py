class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum = 0
        total = sum(nums)

        for idx, num in enumerate(nums):

            right_sum = total - (left_sum + num)

            if right_sum == left_sum:
                return idx
            
            left_sum += num
        
        return -1