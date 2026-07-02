class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        The idea is to get each number in a set and search for that number 
        So, if I iterate my nums list I get a number I check if the number has any numbers ahead of it
        (incrementally)
        or there are numbers behind it decrementally . I traverse the list and then I can get the longest 
        Consecutive Number list . Each time i get a maximum sum , I change the sum to the maximum count

        ''' 
        numSet = set(nums)
        longest = 0
        for num in nums:
            # means there are no numbers behind it (it is start of the sequence) 
            if (num - 1) not in numSet:
                # then we can check if the next number is present 
                length = 0 
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest



