class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        ans = 0
        while l< r:
            pillar1 = heights[l]
            pillar2 = heights[r]
            height = min(pillar1, pillar2)
            ans = max(ans, height*(r-l)) 
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return ans
                     
