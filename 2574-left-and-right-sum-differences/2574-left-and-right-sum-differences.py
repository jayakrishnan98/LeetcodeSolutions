class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = 0
        right_sum = sum(nums)

        for idx, value in enumerate(nums):

            nums[idx] = abs(left_sum - (right_sum - value))

            left_sum += value
            right_sum -= value

        return nums
