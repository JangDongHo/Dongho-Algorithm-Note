class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = {}
        max_len = 0
        start = 0

        for end in range(len(s)):
            c = s[end]
            if c in char_dict:
                start = max(start, char_dict[c] + 1)
            char_dict[c] = end
            max_len = max(max_len, end - start + 1)
        
        return max_len