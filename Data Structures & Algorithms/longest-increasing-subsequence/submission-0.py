class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def traverse(index, prev_index):
            if index >= n:
                return 0
            key = (index, prev_index)
            if key in memo:
                return memo[key]
            not_take = 0 + traverse(index+1, prev_index)
            take = 0
            if prev_index == -1 or nums[index] > nums[prev_index]:
                take = 1 + traverse(index+1, index)
            memo[key]=  max(take, not_take)
            return memo[key]
        return traverse(0, -1)
