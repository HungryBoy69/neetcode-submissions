from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = defaultdict(int) # ABABAA  k = 1 
        j, i = 0, 0
        count_max = 0
        while j < len(s):
            hashMap[s[j]] +=1  # A: 1, B:1 
            while (j - i + 1) - max(hashMap.values()) > k:  # if the 
                hashMap[s[i]]-=1
                i+=1 # we shrink the loop
                print('the character is', s[j], 'at pos', j,'shrinking the left space')
            count_max = max(count_max, j-i+1)
            j +=1
        return count_max