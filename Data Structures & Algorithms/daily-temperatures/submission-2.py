class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Either solve this in a O(n2) or 
        push the elements in the stack . Once you get the number greater you take the diff
        of indices and pop the previous element and push the new number ( viz greater )
       '''
        # ans = []
        # for i in range(0, len(temperatures)-1):
        #     element = temperatures[i]
        #     flag = 1
        #     for j in range( i+1, len(temperatures)):
        #         if element < temperatures[j]:
        #             ans.append(j-i)
        #             flag = 0
        #             break
        #     if flag == 1:
        #         ans.append(0)
        # ans.append(0)
        # return ans 
        res = [0]*len(temperatures)
        stack = []
        for i , t in enumerate(temperatures):
            while stack and t> stack[-1][0]:
                stackT, stackInd =  stack.pop()
                res[stackInd]=i-stackInd
            stack.append((t, i))
        return res 
            