class Solution:
    def rob(self, nums: list[int]) -> int:
        best_two_back = 0
        best_previous = 0

        for money in nums:
            skip_current = best_previous
            rob_current = money + best_two_back

            current_best = max(skip_current, rob_current)

            best_two_back = best_previous
            best_previous = current_best

        return best_previous