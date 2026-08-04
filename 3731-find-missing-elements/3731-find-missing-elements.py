class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums = set(nums)
        return [x for x in range(min(nums), max(nums)) if x not in nums]