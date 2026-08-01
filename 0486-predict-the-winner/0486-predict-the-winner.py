from functools import cache
from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        @cache
        def dp(left: int, right: int) -> int:
            # Only one number remains
            if left == right:
                return nums[left]

            choose_left = nums[left] - dp(left + 1, right)
            choose_right = nums[right] - dp(left, right - 1)

            return max(choose_left, choose_right)

        return dp(0, len(nums) - 1) >= 0