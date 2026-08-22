from collections import defaultdict
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        hashMap = defaultdict(int)
        for ch in s:
            hashMap[ch]+=1
        if hashMap['1'] == 1:
            return '0'*hashMap['0'] + '1'
        else:
            num_one = hashMap['1'] - 1
            return '1'*num_one + '0'*hashMap['0'] + '1'