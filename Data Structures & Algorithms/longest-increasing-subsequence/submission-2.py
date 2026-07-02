class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n = len(nums)
        # memo = {}
        # def traverse(index, prev_index):
        #     if index >= n:
        #         return 0
        #     key = (index, prev_index)
        #     if key in memo:
        #         return memo[key]
        #     not_take = 0 + traverse(index+1, prev_index)
        #     take = 0
        #     if prev_index == -1 or nums[index] > nums[prev_index]:
        #         take = 1 + traverse(index+1, index)
        #     memo[key]=  max(take, not_take)
        #     return memo[key]
        # return traverse(0, -1)
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
