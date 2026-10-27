class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        freq = {0:1}
        prefix_sum = 0

        for num in nums:
            prefix_sum += num

            result += freq.get(prefix_sum - k, 0)

            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1 
        
        return result