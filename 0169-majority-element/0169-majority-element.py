class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hashmap = {}
        max_count = 0
        result = nums[0]
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
            if hashmap[num] > max_count:
                max_count = hashmap[num]
                result = num
        
        return result