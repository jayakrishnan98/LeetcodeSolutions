class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hashmap = {}
        threshold = len(nums)//2
        for num in nums:
            count = hashmap.get(num, 0) + 1
            if count > threshold:
                return num
            hashmap[num] = count