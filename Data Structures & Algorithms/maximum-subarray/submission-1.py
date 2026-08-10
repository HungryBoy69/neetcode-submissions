class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Brute force can be to make all the combination of subarrays
        eg:
         1 2 3 4 
         subarray from 1 till end - max)

        1  
           2   
             3 
               4 
         1 2 3 4
         1 2 3 4
           2 3 4
             3 4        
        ''' 
        max_so_far = nums[0]
        max_ending_here = nums[0]
        for i in range(1, len(nums)):
            max_ending_here = max(nums[i], nums[i]+ max_ending_here)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

