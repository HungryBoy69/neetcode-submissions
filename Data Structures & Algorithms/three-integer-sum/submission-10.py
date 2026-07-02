class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
            Brute force will include taking three loops and finding the sum of the three .

            Or Maybe we can iterate over the array and get a target 
            and then get the other two so that it becomes the negative of the first number 
            pretty much like two sum.
        '''
        nums.sort()
        nums_count = defaultdict(int)
        res = []
        for number in nums:
            nums_count[number]+=1
        for i in range(len(nums)):
            x = []
            for j in range( i+1, len(nums)):
                find_num = - (nums[i]+ nums[j])
                if find_num in nums_count.keys():
                    if (find_num == nums[j] or find_num == nums[j]) and nums_count[find_num]> 1:
                        if find_num == nums[i] == nums[j] and find_num == 0 and nums_count[find_num] <3:
                            continue
                        x = [nums[i],nums[j], find_num]
                    if find_num !=nums[j] and find_num!=nums[i]:
                        x = [nums[i], nums[j], find_num]
                x.sort()
                if x not in res and len(x) > 0:
                    res.append(x)
        return res
                