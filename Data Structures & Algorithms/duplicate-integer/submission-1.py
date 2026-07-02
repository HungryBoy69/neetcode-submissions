class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasMap = []
        for i in nums:
            if i in hasMap:
                return True
            else:
                hasMap.append(i)
        return False
