class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        person_trusts = defaultdict(int)
        is_trusted = defaultdict(int)
        for d,v in trust:
            person_trusts[d]+=1
            is_trusted[v]+=1
        for i in range(1, n+1):
            if i not in person_trusts and is_trusted[i] == n-1:
                return i
        return -1

