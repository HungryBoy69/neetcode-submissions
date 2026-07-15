class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        itr = 0 
        for i in range(0, len(nums)):
            if nums[i]!=0:
                nums[itr] = nums[i]
                itr+=1
        while itr < len(nums):
            nums[itr] = 0
            itr+=1
    
