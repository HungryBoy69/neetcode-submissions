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
'''
sum == target -> means we need to stop because we already found one set of elements. 

We need to maintain the idx because we need to go forward, if we don't then we might get duplicate subsets like [2, 3] andd [3, 2]

Once we know that particular element can be added and would actually help reach the target, we can get the new one with the same idx meaning same element can be added ( ask of the question )

Then, what if the sum + nums[idx] goes out of target, we need to look for new element in that case so idx+1

Once we have added the last element, we can look for a subset without having choosen this particular element, so we do a idx+1 after removing the element from the current array and sum


'''