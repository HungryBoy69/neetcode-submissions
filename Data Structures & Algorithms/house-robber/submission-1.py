class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # memo = {}
        # def traverse(index, visited):
        #     if index >=n:
        #         return 0
        #     rob = 0
        #     key = (index, visited)
        #     if key in memo:
        #         return memo[key]
        #     if not visited:
        #         rob = nums[index] + traverse(index+1, True)
        #     not_rob = 0+ traverse(index+1, False)
        #     memo[key] = max(rob, not_rob)
        #     return memo[key]
        # return traverse(0, False)
        # We create a dp[i] which says max money robbed uptil index i
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[len(nums)-1]