class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1], [1,1]]
        '''
                    1 
                1      1
            1      2      1
        1      3       3     1 
    1       4      6      4      1     



        '''
        idx = 0
        if numRows == 1:
            return [res[0]]
        if numRows == 2:
            return res
        for counter_len in range(3, numRows+1):
            i = 0
            ans = []
            while i <= idx and i < len(res[counter_len - 2]): 
                ans.append(res[counter_len -2][i] + res[counter_len -2 ][i+1])
                i+=1
            res.append([1] + ans + [1])
            idx+=1
        return res

            



