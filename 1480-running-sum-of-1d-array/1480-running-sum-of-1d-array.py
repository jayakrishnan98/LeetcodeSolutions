class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cur_sum = 0
        for i in range(len(nums)):
            value = nums[i]
            cur_sum += value
            nums[i] = cur_sum
        return nums
