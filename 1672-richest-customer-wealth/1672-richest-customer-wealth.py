class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_value = 0
        for item in accounts:
            cur_sum = sum(item)
            max_value = max(cur_sum, max_value)

        return max_value
