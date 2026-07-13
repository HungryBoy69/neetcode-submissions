class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max_num = max(nums)
        if len(nums) == 3:
            if (nums[1] > nums[0]) and (nums[1] > nums[2]):
                return 1
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i-1] and (nums[i]> nums[i+1]):
                return i
        if max_num == nums[0]:
            return 0 
        if max_num == nums[-1]:
            return len(nums)-1
        return -1