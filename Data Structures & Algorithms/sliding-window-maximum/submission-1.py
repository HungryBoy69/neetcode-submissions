class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        i, j = 0,0 
        ans= []
        while j < len(nums):
            while dq and nums[dq[-1]] < nums[j]:
                dq.pop()
            dq.append(j)
            if (j-i+1) == k:
                ans.append(nums[dq[0]])
                if nums[i] == nums[dq[0]]:
                    dq.popleft()
                i+=1
            j+=1
        return ans