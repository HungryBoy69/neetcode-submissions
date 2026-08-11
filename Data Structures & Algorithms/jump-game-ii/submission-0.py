class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i == len(nums) - 1:
                return 0

            if i in memo:
                return memo[i]

            if nums[i] == 0:
                return float("inf")

            furthest = min(len(nums) - 1, i + nums[i])
            result = float("inf")

            for j in range(i + 1, furthest + 1):
                result = min(result, 1 + dfs(j))

            memo[i] = result
            return result

        return dfs(0)