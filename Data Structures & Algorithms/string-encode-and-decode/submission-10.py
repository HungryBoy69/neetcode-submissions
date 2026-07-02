class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ''
        if strs == [""]:
            return ';'

        ans = strs[0]
        for i in range(1, len(strs)):
            ans = ans + ';' + strs[i]
        return ans
    def decode(self, s: str) -> List[str]:
        print(s)
        if s == '':
            return []
        if s == ';':
            return [""]
        return s.split(';')