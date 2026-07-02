class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''

        Okay we need something such that when i traverse an element i know what is the next greater element
        ahead of it.What if i tarverse backwards
        TheN i have a greater number then I go back to another number let say smaller than it 
        then i go to another number smaller than that so how should I identify which one should
        be the right side boundary.
        '''
        '''
        One such approach is to traverse in a O(n2) fashion such that for every element I can go 
        and find the next greater element and give back the result for it . 
        Let's code this up and check the results first .'''
        ans = []
        for i in range(0, len(temperatures)-1):
            element = temperatures[i]
            flag = 1
            for j in range( i+1, len(temperatures)):
                if element < temperatures[j]:
                    ans.append(j-i)
                    flag = 0
                    break
            if flag == 1:
                ans.append(0)
        ans.append(0)
        return ans 