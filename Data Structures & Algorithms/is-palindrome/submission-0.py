import re 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
            You can use either st = re.sub(r"[^\w\d]", "", s)
            or you can check the string's alphanumeric character
            by using str.isalnum()
        '''
        new_string = ''
        for st in s:
            if st.isalnum():
                new_string += st.lower()
        
        for i in range(0, int(len(new_string)/2)):
            if new_string[i].lower() != new_string[len(new_string)-(i+1)].lower():
                print(new_string[i], s[len(new_string)- (i+1)], i)
                return False
        return True

        