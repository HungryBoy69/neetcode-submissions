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