class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = cost[-2], cost[-1]
        for i in range(len(cost) - 3, -1, -1):
            one, two = cost[i] + min(one, two), one
        return min(one, two)
