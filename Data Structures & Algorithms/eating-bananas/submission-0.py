class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)
        res = end
        while start <=end:
            rate = (start+end)//2

            total_time = 0
            for p in piles:
                total_time += math.ceil(p/rate)
            if total_time <=h:
                res = rate
                end = rate-1
            else:
                start = rate+1
        return res