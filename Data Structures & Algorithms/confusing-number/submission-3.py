class Solution:
    def confusingNumber(self, n: int) -> bool:
        not_confusing = [2,3,4,5,7]
        str_n = str(n)
        for ch in str_n:
            if int(ch) in not_confusing:
                return False
        mapping  = {'6': '9', '9': '6'}
        rev_str  = str_n[::-1]
        new_str = ''
        for i in range(len(rev_str)):
            new_str+= mapping.get(rev_str[i], rev_str[i])
        return  new_str != str_n
