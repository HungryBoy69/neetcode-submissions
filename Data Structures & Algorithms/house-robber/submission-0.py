class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def traverse(index, visited):
            if index >=n:
                return 0
            rob = 0
            key = (index, visited)
            if key in memo:
                return memo[key]
            if not visited:
                rob = nums[index] + traverse(index+1, True)
            not_rob = 0+ traverse(index+1, False)
            memo[key] = max(rob, not_rob)
            return memo[key]
        return traverse(0, False)