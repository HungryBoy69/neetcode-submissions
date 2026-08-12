class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_elem  = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            temp_val = max_elem
            max_elem = max(max_elem, arr[i])
            arr[i]= temp_val
        arr[-1] = -1 
        return arr