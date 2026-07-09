class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        '''
            1 2 3 4 5 6

            5 6 1 2 3 4

            4 5 6 1 2 3   1 > nums

            3 4 5 6 1 2
        '''
        low = 0
        high = len(nums)-1
        while low <= high:

            mid = (low+high)//2
            if nums[mid] == target:
                return True
            if nums[low] < nums[mid]: # rotated array check to the left
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[low] > nums[mid]: # we have to check in right side
                if nums[mid] < target <=nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                low +=1
        return False 
