class Solution:
    def climbStairs(self, m: int) -> int:
        nums = []
        memo = {}
        for i in range(0, m+1):
            nums.append(i)
        n = len(nums)

        def traverse(index):
            if index >=n:
                return 0
            if index  in memo:
                return memo[index]
            if index == n-1:
                return 1
            memo[index] = traverse(index+1) + traverse(index+2)
            return memo[index]
        return traverse(0)