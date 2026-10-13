class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}

        for idx, num in enumerate(nums):

            compliment = target - num

            if compliment in hashmap:
                return [hashmap[compliment], idx]
            
            hashmap[num] = idx
        

            