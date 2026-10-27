class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        hashmap = {}
        for idx, value in enumerate(numbers):
            complement = target - value
            print(complement)

            if complement in hashmap:
                return [hashmap[complement], idx+1]
            
            hashmap[value] = idx+1
        
