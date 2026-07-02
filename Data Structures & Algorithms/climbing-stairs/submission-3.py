class Solution:
    def climbStairs(self, m: int) -> int:
        # nums = []
        # memo = {}
        # for i in range(0, m+1):
        #     nums.append(i)
        # n = len(nums)
        # def traverse(index):
        #     if index >=n:
        #         return 0
        #     if index  in memo:
        #         return memo[index]
        #     if index == n-1:
        #         return 1
        #     memo[index] = traverse(index+1) + traverse(index+2)
        #     return memo[index]
        # return traverse(0)
        n = m
        if n == 0:
            return 1
        if n == 1:
            return 1

        dp = [0] * (n + 1)  # will give 0 1, 2 for n =2 

        dp[0] = 1 # for dp[0] is 1 since no steps required for stair 0 ( do nothing )
        dp[1] = 1 # for first step one way to use the 1 step and be on step 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]