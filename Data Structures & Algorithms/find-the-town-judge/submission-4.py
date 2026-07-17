class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        delta = defaultdict(int)
        '''
        judge trusts no body 
        and is trusted by everyone except self
        so if I maintain counter like each time somebody trusts someone I decrease
        the counter but when someone trusts me I increase the counter
        so if that's the case for the judge index the answer would be exactly 
        n - 1
        '''
        for d,v in trust:
            delta[d]-=1
            delta[v]+=1
        for i in range(1, n+1):
            if delta[i] == n-1:
                return i
        return -1

