class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        result = 0
        left, right = -1, 0
        freq = Counter()
        while right < len(nums):
            freq[nums[right]] += 1
            while freq[nums[right]] > k:
                left += 1
                freq[nums[left]] -= 1
            result = max(result, right-left)
            right += 1
        return result
