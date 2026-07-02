class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_num  =  "".join(str(x) for x in digits)
        return list(str(int(str_num) + 1))