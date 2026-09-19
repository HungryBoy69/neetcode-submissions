class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def check_if_palindrome(sub_str):
            for i in range(0, len(sub_str)//2):
                if sub_str[i] != sub_str[len(sub_str) - i-1]:
                    return False
            return True
        ans = []
        def traverse(idx, current):
            if idx >= len(s):
                ans.append(current.copy())
                return
            
            for j in range(idx, len(s)):
                sub_str = s[idx:j+1]
                if check_if_palindrome(sub_str):
                    current.append(sub_str)
                    traverse(j+1, current)
                    current.pop()
        traverse(0, [])
        return ans
    """
        we are deciding to put the partition,
        so for every idx that we are moving forward we decide in 
        idx till the len of array where can we take that substring 
        with us. for each substr we decide if the substr we took out 
        is a palindrome or not
        once confirmed we add that to out current result,
        recursively ( try all options of slicing from the idx till the len of array )move ahead to the next index of what we have sliced. In this way we have stored the reuslt "aa" now we move to the next index in the array which is b ( aab ). 
    """