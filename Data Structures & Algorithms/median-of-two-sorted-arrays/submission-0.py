class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 =nums1 + nums2 
        nums3.sort()
        size_arr = len(nums3)
        if size_arr%2 == 0:
            first_num = size_arr//2
            print('first-second', first_num)
            second_num = first_num - 1 
            print('first-second', second_num)
            print('the value is', int(nums3[first_num]+ nums3[second_num]))
            return float(int(nums3[first_num]+ nums3[second_num])/2)
        else:
            print('first', size_arr//2)
            return float(nums3[size_arr//2])