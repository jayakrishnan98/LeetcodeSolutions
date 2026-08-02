from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]

        for index in range(n):
            dp[index][index] = piles[index]

        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1

                take_left = piles[left] - dp[left + 1][right]
                take_right = piles[right] - dp[left][right - 1]

                dp[left][right] = max(take_left, take_right)

        return dp[0][n - 1] > 0