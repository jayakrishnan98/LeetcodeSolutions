class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        maj_count = len(nums) // 2
        freq = {}
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] > maj_count:
                return num
