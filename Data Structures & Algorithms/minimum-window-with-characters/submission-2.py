from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashMap = defaultdict(int)
        for i in range(0, len(t)):
            hashMap[t[i]]+=1
        distFreq = len(hashMap)
        i, j = 0, 0
        min_len = float("inf")
        ans = (-1, -1)
        while j < len(s):
            if s[j] in hashMap:
                hashMap[s[j]]-=1
                if hashMap[s[j]] ==0:
                    distFreq -=1
            
            while distFreq == 0:
                if j - i + 1 < min_len:
                    min_len = j - i + 1
                    ans = (i, j)
                if s[i] in hashMap:
                    if hashMap[s[i]] ==0:
                        distFreq+=1
                    hashMap[s[i]]+=1
                i+=1
            j+=1
        if ans == (-1, -1):
            return ""
        return s[ans[0]:ans[1]+1]
                
                
