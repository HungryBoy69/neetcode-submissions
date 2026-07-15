class Solution:
    def scoreOfString(self, s: str) -> int:
        '''
        ch = 'A'
        print(ord(ch))
        ''' 
        ans= 0  
        for i in range(1, len(s)):
            ans += abs(ord(s[i]) - ord(s[i-1]))
        return ans
