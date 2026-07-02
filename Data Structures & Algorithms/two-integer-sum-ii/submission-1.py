class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
            100 50 20 15 10 3 2 1
            1 2 3 10 15 20 50 100
            target = 4  [1,2,2] indices 1,2 are not equal 
            O(n^2)
            Return indices.
        '''
        x = {}
        for i in range(0, len(numbers)):
            if numbers[i] in x.keys():
                x[numbers[i]] = [x[numbers[i]][0]+1, i]
            else: 
                x[numbers[i]] = [1, i]
        for num in numbers:
            find_num = target - num
            if find_num in x.keys():
                if find_num == num and x[num][0] > 1:
                    return [x[num][1]+1, x[num][1]+1]
                else:
                    return [x[num][1]+1, x[find_num][1]+1]