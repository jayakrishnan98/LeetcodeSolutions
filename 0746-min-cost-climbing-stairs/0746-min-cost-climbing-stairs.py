class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        minimum_cost = [0] * ( n+1 )
        for i in range(2, n+1):
            one_step = minimum_cost[i-1] + cost[i-1]
            two_step = minimum_cost[i-2] + cost[i-2]

            minimum_cost[i] = min(one_step, two_step)
        
        return minimum_cost[n]