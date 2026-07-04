class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        for num in nums:
            if num in hashMap:
                hashMap[num]+=1
            else:
                hashMap[num] =1 
        for d,v in hashMap.items():
            if v > len(nums)/2:
                return d