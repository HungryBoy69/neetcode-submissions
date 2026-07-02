class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        def traverse(index):
            if index >= n:
                return 0
            if index in memo:
                return memo[index]
            memo[index] =cost[index] + min(traverse(index+1) , traverse(index+2))
            return memo[index]
        return min(traverse(0), traverse(1))