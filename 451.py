class Solution:
    def frequencySort(self, s: str) -> str:
        char_freq = {}
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1
        
        sorted_chars = sorted(char_freq.keys(), key=lambda x: char_freq[x], reverse=True)
        
        sorted_string = ""
        for char in sorted_chars:
            sorted_string += char * char_freq[char]
        
        return sorted_string
