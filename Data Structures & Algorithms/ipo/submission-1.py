class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # prof_cap = []
        # for i in range(len(profits)):
        #     prof_cap.append(( capital[i], profits[i] ))  # one loop
        
        # while k > 0:
        #     # we need to take out projects which are currently eligible based on the capital we have and out of those do the one which has maxium profit
        #     eligible_projects = [item for item in prof_cap if  w>= item[0]]   #second loop
        #     if not eligible_projects:
        #         break
        #     eligible_projects = sorted(eligible_projects, key = lambda x:x[1], reverse = True)  #third loop
        #     # now pick the first item and let's do it again and again
        #     best = eligible_projects[0]
        #     w+=eligible_projects[0][1]
        #     prof_cap.remove(best)
        #     k-=1
        # return w   
        '''
            now instead of doing this again and again what if I was able to retrieve the best projects ordered by 
            for me. This points me to the direction of using a heap
        '''
        prof_cap = list(zip(capital, profits))
        maxProfit = []
        heapq.heapify(prof_cap)
        for i in range(k):
            while prof_cap and prof_cap[0][0] <= w:
                c, p = heapq.heappop(prof_cap)
                heapq.heappush(maxProfit, -1* p)
            if not maxProfit:
                break
            w += -1 * (heapq.heappop(maxProfit))
        return w