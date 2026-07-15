class Solution:
    def isPalindrome(self, x: int) -> bool:
        s= str(x)
        print(s[::-1])
        return s  == s[::-1]