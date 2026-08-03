class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2

        for stair in range(3, n+1):
            dp[stair] = dp[stair - 1] + dp[stair - 2]

        return dp[n]