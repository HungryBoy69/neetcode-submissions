class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = {}
        def traverse(i, flag):
            if i == len(nums)-1:
                return max(0, nums[i]) if flag else nums[i]
            key = (i, flag)
            if key in memo:
                return memo[key]
            if flag: # started my subarray then
                memo[key] = max(0, nums[i] + traverse(i+1, True))
            else:
                choosen = traverse(i+1, True) + nums[i]
                not_chosen = traverse(i+1, False) 
                memo[key]= max(choosen, not_chosen)
            return memo[key]
        return traverse(0, False)

