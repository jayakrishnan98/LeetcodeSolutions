class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        n = len(nums)

        min_value_idx = nums.index(min(nums))
        max_value_idx = nums.index(max(nums))

        min_index = min(min_value_idx, max_value_idx)
        max_index = max(min_value_idx, max_value_idx)

        return min(max_index+1, min_index + 1 + n - max_index, n-min_index)