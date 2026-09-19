class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def _permute(nums, current=[]):
            if len(current) == len(nums):
                return [current]
            
            result = []
            for num in nums:
                if num not in current:  # skip numbers already used in this path        
                    result +=_permute(nums, current + [num])
            return result
        return _permute(nums)
        