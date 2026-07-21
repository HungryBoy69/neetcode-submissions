class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0 
        new_str = ''
        while i < len(abbr):
            digit = ''
            if abbr[i].isdigit():
                while i < len(abbr) and abbr[i].isdigit():
                    digit += abbr[i]
                    i+=1
                new_str += '!'*int(digit)
                if digit[0] == '0':
                    return False
                digit = ''
            else:
                new_str+=abbr[i]
                i+=1
        print(new_str)
        if len(new_str) != len(word):
            return False
        for i in range(len(new_str)):
            if word[i]!= new_str[i] and new_str[i]!='!':
                return False
        return True