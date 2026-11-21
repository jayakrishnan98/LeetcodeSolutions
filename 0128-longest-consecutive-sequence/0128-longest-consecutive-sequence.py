class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        best = 0

        for num in nums:
            if num - 1 not in nums:
                nxt = num + 1
                while nxt in nums:
                    nxt += 1
                best = max(best, nxt - num)
        return best