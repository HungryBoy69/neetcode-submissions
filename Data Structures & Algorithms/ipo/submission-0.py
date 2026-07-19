class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        '''

        intuition is to find the maximum capital to take k distinct projects

        k = 3 , w = 0
        profits = [ 1, 4, 2, 3]
        capital = [ 0, 3, 1, 1]

        output = 8  
        we can pick only max of k projects
        w = initial capital
        profit gets added to my capital
        maximum final capital ( w ? is what we need to return )

        create a list of tuples with profits and capital

        How do we determine which project to choose, we can be greedy and pick the highest profit
        '''
        prof_cap = []
        for i in range(len(profits)):
            prof_cap.append(( capital[i], profits[i] ))
        
        while k > 0:
            # we need to take out projects which are currently eligible based on the capital we have and out of those do the one which has maxium profit
            eligible_projects = [item for item in prof_cap if  w>= item[0]]
            if not eligible_projects:
                break
            eligible_projects = sorted(eligible_projects, key = lambda x:x[1], reverse =  True)
            # now pick the first item and let's do it again and again
            best = eligible_projects[0]
            w+=eligible_projects[0][1]
            prof_cap.remove(best)
            k-=1
        return w   