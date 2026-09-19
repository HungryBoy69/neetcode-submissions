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

        We use backtracking to try every possible way to partition the string.

At any point, idx represents the first character that has not yet been included in the current partition. Starting at idx, we try every substring ending from idx through the last character of the string.

For each candidate substring s[idx:j+1], we check whether it is a palindrome. If it is, we add it to the current partition and recursively continue from index j + 1, because all characters through index j have now been used.

When the recursive call returns, we remove the substring we just added. This is the backtracking step, which allows us to try a different substring starting at the same index.

Once idx reaches len(s), every character has been included in the partition, so we copy the current partition into the answer.

Example: s = "aab"
Initially:

idx = 0
current = []
We try substrings starting at index 0:

Choose "a":

current = ["a"]
Recurse from index 1.

From index 1, choose "a":

current = ["a", "a"]
Recurse from index 2.

From index 2, choose "b":

current = ["a", "a", "b"]
We reach the end, so save this partition.

["a", "a", "b"]
Then backtrack by removing "b", and later remove the second "a".

Back at index 0, try "aa":

current = ["aa"]
Since "aa" is a palindrome, recurse from index 2.

From index 2, choose "b":

current = ["aa", "b"]
We reach the end and save:

["aa", "b"]
"aab" is not a palindrome, so it is skipped.

The final result is:

[
    ["a", "a", "b"],
    ["aa", "b"]
]
    """