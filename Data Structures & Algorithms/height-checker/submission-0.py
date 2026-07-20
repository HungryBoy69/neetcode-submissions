class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        '''
        non decreasing means either increasing or same
        '''
        count =0
        new_heights = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != new_heights[i]:
                count+=1
        return count

