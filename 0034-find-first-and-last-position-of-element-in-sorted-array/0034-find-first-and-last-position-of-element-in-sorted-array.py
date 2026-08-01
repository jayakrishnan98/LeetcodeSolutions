from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = bisect_left(nums, target)

        if first == len(nums) or nums[first] != target:
            return [-1, -1]

        last = bisect_right(nums, target) - 1

        return [first, last]