class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        num_prev = nums[0]
        for i in range(0, len(nums)):
            if i%2==0: #even it means the odd one should match
                num_prev= nums[i]
            elif num_prev!=nums[i]:
                return num_prev
        return nums[-1]
        
