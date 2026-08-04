class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:

        result = []
        for item in range(min(nums), max(nums)+1):
            if item not in nums:
                result.append(item)
        return result