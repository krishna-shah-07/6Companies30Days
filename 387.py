class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_freq = {}
        
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1
        
        for i in range(len(s)):
            if char_freq[s[i]] == 1:
                return i
        
        return -1
