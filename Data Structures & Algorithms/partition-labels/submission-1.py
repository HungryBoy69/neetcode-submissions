from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count, i =0, 0
        hashMap = defaultdict(int)
        for iter in range(len(s)):
            hashMap[s[iter]] = iter# stores the max index each time
        max_index = hashMap[s[0]]
        ans = []
        while i <= len(s)-1: # gives each element's max_index 
            max_index = max(max_index, hashMap[s[i]])
            if max_index == i:
                ans.append(len(s[count:i+1]))
                count = i + 1
            i+=1
        return ans
            



