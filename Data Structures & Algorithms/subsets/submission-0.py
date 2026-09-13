class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans  = []
        def traverse(visited, idx, current):

            if idx >= len(nums):
                ans.append(current.copy())
                return 
            visited.add(nums[idx])
            current.append(nums[idx])
            traverse(visited, idx+1,current)

            # remove the current and un mark the visited element
            current.pop()
            visited.remove(nums[idx])
            traverse(visited, idx+1, current)
        traverse(set(), 0, [])
        return ans

