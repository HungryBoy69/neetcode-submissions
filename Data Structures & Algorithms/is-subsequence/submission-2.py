class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        memo = {}
        def traverse(i, j):
            if i == len(s):
                return True
            if j == len(t):
                return False
            key = (i, j)
            if key in memo:
                return memo[key]
            if s[i] == t[j]:
                memo[key] = traverse(i+1, j+1)
                return memo[key]
            memo[key] = traverse(i, j+1)
            return memo[key]
        return traverse(0,0)
            