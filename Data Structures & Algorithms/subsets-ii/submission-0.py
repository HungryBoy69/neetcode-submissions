class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        def traverse(idx, current):
            if idx >=len(nums):
                key = (tuple(sorted(current)))
                ans.add(key)
                return 
            
            current.append(nums[idx])
            traverse(idx+1, current)
            current.pop()
            traverse(idx+1, current)
        traverse(0, [])
        ans = [list(x) for x in ans]
        return ans