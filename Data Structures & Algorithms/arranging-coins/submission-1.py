class Solution:
    def arrangeCoins(self, n: int) -> int:
        iter = 0
        ans = 0
        while n > 0:  #true  4
            n -= iter+1  
            if n >= 0:
                ans+=1
            iter+=1
        return ans