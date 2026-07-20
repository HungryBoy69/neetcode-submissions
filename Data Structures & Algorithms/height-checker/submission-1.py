class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        '''
        non decreasing means either increasing or same
        '''
        count = [0]* 101
        new_array = []
        for num in heights:
            count[num]+=1
        for num in range(1, 101):
            count_num = count[num]
            for _ in range(count_num):
                new_array.append(num)
        
        res = 0 
        for i in range(0, len(heights)):
            if heights[i]!=new_array[i]:
                res+=1
        return res

