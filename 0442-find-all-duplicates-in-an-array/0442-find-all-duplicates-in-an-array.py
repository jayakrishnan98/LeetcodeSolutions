class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        or_set = set()
        result = []
        for num in nums:
            if num not in or_set:
                or_set.add(num)
            else:
                result.append(num)
        
        return result