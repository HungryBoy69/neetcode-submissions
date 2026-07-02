class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        start, end = 0, len(nums)-1 
        while start <=end:
            mid = (start+end)//2

            res = min(res, nums[mid])
            if nums[mid]> nums[end]:
                start = mid +1
                res = min(res, nums[mid])
            else:
                end = mid-1
                res = min(res, nums[mid])
        return res