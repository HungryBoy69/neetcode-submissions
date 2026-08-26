class Solution:
    def convertToTitle(self, colNumber: int) -> str:
        ans  = ''
        while colNumber !=0:
            num = (colNumber -1 ) % 26
            ans += chr(num + ord('A'))
            colNumber = (colNumber -1 ) // 26
        return ans[::-1]
        