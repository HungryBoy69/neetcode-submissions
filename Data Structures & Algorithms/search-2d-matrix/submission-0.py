class Solution:

    def search(self, nums: List[int], target: int) -> int:
        low , high = 0, len(nums) -1 

        while low <=high:
            mid = (low + high) // 2
            print(mid)
            if nums[mid] == target:
                return True 
            elif nums[mid] < target:
                low = mid+1
            elif nums[mid] > target:
                high = mid -1 
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix_list = []
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                matrix_list.append(matrix[i][j])
        return self.search(matrix_list, target)