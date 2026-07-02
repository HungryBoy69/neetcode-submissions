class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        '''
            We check if left half is sorted or right half is sorted. once we decide, we move to that space 
            and then check if the element is present there or not..
            
        '''
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            
            # Left half is sorted
            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        
        return -1
