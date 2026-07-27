class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows -1): # nums is 2 then 1  then 0 eligible 
            temp = [0] + res[-1] + [0] #last wala element [0] + [1] + [0]
            row = []
            for j in range(len(res[-1])+1): # 2 -> 0, 1 
                row.append(temp[j]+ temp[j+1])
            res.append(row)  # in a way backfilling logic to easily add numbers
        return res

            



