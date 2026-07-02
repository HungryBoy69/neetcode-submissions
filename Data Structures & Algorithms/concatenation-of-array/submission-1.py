class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0, len(nums)):
           nums.append(nums[i])
        return nums