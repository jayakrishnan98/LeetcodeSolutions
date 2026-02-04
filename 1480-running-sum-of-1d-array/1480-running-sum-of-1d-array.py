class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        resp = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(i + 1):
                resp[i] = resp[i] + nums[j]
        return resp