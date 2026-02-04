class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        leng = len(nums)
        resp = [0] * (2 * leng)
        for i in range(leng):
            resp[i] = nums[i]
            resp[i+leng] = nums[i]
        return resp