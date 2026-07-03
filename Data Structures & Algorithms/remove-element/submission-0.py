class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = []
        for num in nums:
            if num != val:
                print(num)
                ans.append(num)
        for i in range(len(ans)):
            nums[i] = ans[i]
        return len(ans)

         