class Solution:
    def maxScore(self, s: str) -> int:
        prefix_zeroes = [0]* len(s)
        suffix_ones = [0] * len(s)
        count_zero , count_one= 0, 0
        for i in range(len(s)):
            if s[i] == '0':
                count_zero +=1
            prefix_zeroes[i] = count_zero
        for i in range(len(s)-1, -1, -1):
            if s[i] == '1':
                count_one+=1
            suffix_ones[i] = count_one
        res = 0
        print(suffix_ones)
        print(prefix_zeroes)
        for i in range(0, len(s)-1):
                res = max(suffix_ones[i+1]+prefix_zeroes[i], res) 
        return res
            
                        