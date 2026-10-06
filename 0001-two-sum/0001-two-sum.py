class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}

        for i in range(len(nums)):

            compliment = target - nums[i]
            if compliment in hashmap:
                return [hashmap[compliment], i]
            
            hashmap[nums[i]] = i
        
        print(hashmap)
        

            