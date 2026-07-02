class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_size = len(s1)
        i = 0
        s1 = sorted(s1)
        while i <= len(s2):
            print(s1_size + i , 'for i', i)
            if (s1_size + i ) <= len(s2):
                sub_str = s2[i:i+s1_size]
                sub_str = sorted(sub_str)
                print(sub_str, s1)
                if sub_str == s1:
                    return True
            i+=1
        return False