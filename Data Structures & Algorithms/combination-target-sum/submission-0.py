class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def traverse(current, idx, sum):
            if idx >= len(nums):
                if sum == target:
                    ans.append(current.copy())
                return
            add = False
            if sum + nums[idx] <= target:
                current.append(nums[idx])
                sum+= nums[idx]
                traverse(current, idx, sum)
                add = True
            else:
                traverse(current, idx+1, sum)
            if add:
                current.pop()
                sum-=nums[idx]
                traverse(current, idx+1, sum)
        traverse([], 0, 0)
        return ans