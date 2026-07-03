class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # ["bag", "banana", "band"]   it =3
        # ["banana", "bang", "banter"] it = 7
        for i in range(0, len(strs[0])):
            first_str_char = strs[0][i]  # b
            for s in range(1, len(strs)):
                if  i >= len(strs[s]) or strs[s][i] != first_str_char : #banana b != first_str_char
                    return  strs[0][:i]
        return strs[0]

