class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        n = len(s)

        for i in range(n):
            char_set = set()
            current_length = 0

            for j in range(i, n):
                if s[j] not in char_set:
                    char_set.add(s[j])
                    current_length += 1
                    max_length = max(max_length, current_length)
                else:
                    break  # Stop when duplicate found

        return max_length
