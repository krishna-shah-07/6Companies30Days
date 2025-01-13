class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def get_prefix_array(pattern):
            prefix_array = [0] * len(pattern)
            j = 0
            for i in range(1, len(pattern)):
                while j > 0 and pattern[i] != pattern[j]:
                    j = prefix_array[j - 1]
                if pattern[i] == pattern[j]:
                    j += 1
                prefix_array[i] = j
            return prefix_array

        def kmp_search(text, pattern, prefix_array):
            beautiful_indices = []
            j = 0
            for i in range(len(text)):
                while j > 0 and text[i] != pattern[j]:
                    j = prefix_array[j - 1]
                if text[i] == pattern[j]:
                    j += 1
                if j == len(pattern):
                    beautiful_indices.append(i - len(pattern) + 1)
                    j = prefix_array[j - 1]
            return beautiful_indices

        prefix_a = get_prefix_array(a)
        prefix_b = get_prefix_array(b)
        beautiful_indices = []

        matches_a = kmp_search(s, a, prefix_a)
        matches_b = kmp_search(s, b, prefix_b)

        for idx_a in matches_a:
            for idx_b in matches_b:
                if abs(idx_a - idx_b) <= k:
                    beautiful_indices.append(idx_a)
                    break  # Move to the next idx_a once a beautiful index is found

        return beautiful_indices
