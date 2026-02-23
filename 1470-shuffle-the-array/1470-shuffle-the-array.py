class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        outArray = []
        for i in range(n):
                outArray.append(nums[i])
                outArray.append(nums[i+n])
        return outArray