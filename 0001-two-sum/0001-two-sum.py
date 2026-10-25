class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}

        for index, value in enumerate(nums):
            complement = target - value
            if complement in hashmap:
                return [hashmap[complement], index]
            
            hashmap[value] = index