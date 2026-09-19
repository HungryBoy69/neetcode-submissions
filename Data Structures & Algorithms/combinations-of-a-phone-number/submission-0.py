class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        hashMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        ans = []

        def traverse(idx, current):

            if len(current) >= len(digits):
                ans.append(current)
                return
           
            digit = digits[idx]
            for ch in hashMap[digit]:
                traverse(idx+1, current+ch)
        # '0 1 2 3'
        if digits:
            traverse(0, "")
        return ans
     # ' i = 0 get [34] mei se 3 '
            # 3 is the digit , now look up the digit -> "def" now take one and go to next digit, now take the set of chars in that keypad digit and build new digit




